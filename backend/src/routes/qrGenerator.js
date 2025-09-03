// /utils/qrGenerator.js
const QRCode = require('qrcode');

const generateQR = async (data) => {
    try {
        // The data can be a simple string (like a booking ID) or a URL
        // pointing to the ticket verification page.
        // Example: https://your-website.com/verify?ticketId=UNIQUE_ID
        const qrCodeDataURL = await QRCode.toDataURL(JSON.stringify(data));
        return qrCodeDataURL;
    } catch (err) {
        console.error('Error generating QR code', err);
        throw err; // Propagate error to be handled by the caller
    }
};

module.exports = { generateQR };