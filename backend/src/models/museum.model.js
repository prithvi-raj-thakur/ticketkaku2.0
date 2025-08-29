import mongoose from "mongoose";
const museumSchema = new mongoose.Schema({
  _id:{type: String, required: true},
  name: {type: String, required: true},
  location: {type: String, required: true},
  description: {type: String, required: true},
  image: {type: String, required: true},
  price:{type:Array, required:true},
  openingTime:{type:String, required:true},
  closingTime:{type:String, required:true},
  dayoff:{type:String, required:true},
  category:{type:String, required:true}
},{timestamps:true});

const Museum = mongoose.model('Museum', museumSchema);
export default Museum;