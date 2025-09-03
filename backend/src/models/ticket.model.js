import mongoose from "mongoose";

const ticketSchema = new mongoose.Schema({
    visitorName: {
        type: String,
        required: true,
    },
    museumName: {
        type: String,
        required: true,
    },
    visitDate: {
        type: Date,
        required: true,
    },
    numberOfTickets: {
        type: Number,
        required: true,
        min: 1,
    },
    bookingId: {
        type: String,
        required: true,
        unique: true,
    },
    qrCodeUrl: {
        type: String, // We will store the QR code as a Data URL
        required: true,
    },
}, {timestamps: true});

module.exports = mongoose.model('Ticket', ticketSchema);