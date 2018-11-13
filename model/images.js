/*********************************************************
DO WORK HERE PART 1!
This model connects to the 'images' table in your database.
This will be a similar connection to the other models also
found in this folder. Examine the database schema that you
imported and add functionality to this file to allow
it to function like the other models. Make sure that you
export this model so that the data in it can be used in the
rest of the application.
*********************************************************/

var	db = require('../db');
var sequelize = db.sequelize;
var Sequelize = db.Sequelize;

var Images = sequelize.define('images', {
	imageId: {type: Sequelize.INTEGER, primaryKey: true, autoIncrement: true},
	imagePath: Sequelize.STRING,
	imageApproved: Sequelize.STRING,
	altText: Sequelize.STRING,
  userId: Sequelize.INTEGER,
	numLikes: Sequelize.INTEGER,
	uploaded: Sequelize.BOOLEAN,
  createdAt: Sequelize.DATE,
	updatedAt: Sequelize.DATE
})

module.exports = Images; //this exports the model from this page to whatever page imports it
