/*************************************************************************
Fill out this file with Sequelize database connection information.
Make sure that you "export" (make externally available) the resources that
you create in this file. You should need no more than about 4 lines of code
in this file. You should read the documentation referenced on the lab specs
before attempting to create this connection file. If you took IT210A, this
will be similar to the database connection file you made for PHP in Lab 3.
**************************************************************************/

const Sequelize = require('sequelize');
const sequelize = new Sequelize('it210b', 'jwadams', 'oldmanjohnson', {
  host: 'localhost',
  dialect: 'mysql',
  operatorsAliases: false,

  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000
  },
});

var db = {};

db.sequelize = sequelize;
db.Sequelize = Sequelize;

module.exports = db;
