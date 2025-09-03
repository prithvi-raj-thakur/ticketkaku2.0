// /routes/api.js
const express = require('express');
const router = express.Router();
const { v4: uuidv4 } = require('uuid');

// Import all models
const Ticket = require('../models/ticket');
const Museum = require('../models/museum');
const User = require('../models/user'); // Assuming you'll add auth routes later

const { generateQR } = require('../utils/qrGenerator');

// --- Museum Routes ---

// GET /api/museums - Get a list of all museums
router.get('/museums', async (req, res) => {
    try {
        const museums = await Museum.find({}, 'name location ticketPrice imageUrl'); // Only select certain fields
        res.status(200).json(museums);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching museums.' });
    }
});

// POST /api/museums - Add a new museum (for admin purposes)
router.post('/museums', async (req, res) => {
    try {
        const newMuseum = new Museum(req.body);
        await newMuseum.save();
        res.status(201).json(newMuseum);
    } catch (error) {
        res.status(400).json({ message: 'Error creating museum', error: error.message });
    }
});


// --- Ticket Routes ---

// POST /api/book - Create a new ticket
router.post('/book', async (req, res) => {
    try {
        const { visitorName, museumName, visitDate, numberOfTickets } = req.body;

        // 1. Validation
        if (!visitorName || !museumName || !visitDate || !numberOfTickets) {
            return res.status(400).json({ message: 'All fields are required.' });
        }

        // Check if the museum exists in the database
        const museumExists = await Museum.findOne({ name: museumName });
        if (!museumExists) {
            return res.status(404).json({ message: `Museum '${museumName}' not found. `});
        }

        // 2. Generate unique booking ID
        const bookingId = uuidv4();

        // 3. Data for the QR code
        const qrData = {
            bookingId: bookingId,
            visitor: visitorName,
            museum: museumName,
            date: visitDate,
            tickets: numberOfTickets
        };

        const qrCodeUrl = await generateQR(qrData);

        // 4. Create and save the new ticket
        const newTicket = new Ticket({
            visitorName,
            museumName,
            visitDate,
            numberOfTickets,
            bookingId,
            qrCodeUrl,
        });

        await newTicket.save();

        res.status(201).json(newTicket);

    } catch (error) {
        console.error('Booking error:', error);
        res.status(500).json({ message: 'Server error during booking.' });
    }
});

// GET /api/ticket/:bookingId - Fetch a ticket by its bookingId
router.get('/ticket/:bookingId', async (req, res) => {
    try {
        const ticket = await Ticket.findOne({ bookingId: req.params.bookingId });
        if (!ticket) {
            return res.status(404).json({ message: 'Ticket not found.' });
        }
        res.status(200).json(ticket);
    } catch (error) {
        res.status(500).json({ message: 'Server error.' });
    }
});


module.exports = router;