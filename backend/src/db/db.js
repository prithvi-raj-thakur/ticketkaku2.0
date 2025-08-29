import mongoose from "mongoose";
const connectDB = async ()=>{
    try {
        mongoose.connection.on('connected',()=>{
            console.log('Database is connected');
            
        })
        await mongoose.connect(`${process.env.MONGODB_URI}/ticketkaku2`)
    } catch (error) {
        console.error(`Error connecting to MongoDB: ${error.message}`);
    }
}
export default connectDB