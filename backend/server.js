import express from 'express';
import cors from 'cors';
import 'dotenv/config';
import connectDB from './src/db/db.js';
import { clerkMiddleware } from '@clerk/express'
import { serve } from "inngest/express";
import { inngest, functions } from "./src/inngest/inngest.js";


const app = express();

//middleware
app.use(cors());
app.use(express.json());
app.use(clerkMiddleware())


app.get('/', (req, res) => {
  res.send( 'Hello from the backend!' );
});

// Set up the "/api/inngest" (recommended) routes with the serve handler
app.use("/api/inngest", serve({ client: inngest, functions }));

const PORT = process.env.PORT || 3000;
await connectDB();

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
