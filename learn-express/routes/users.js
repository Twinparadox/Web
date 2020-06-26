var express = require('express');
var router = express.Router();


router.get('/:id', function(req, res, next) {
  console.log(req.params, req.query);
  res.send('respond with a resource');
});

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

module.exports = router;
