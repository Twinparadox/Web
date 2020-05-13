var express = require('express');
const {PythonShell} = require('python-shell');
var router = express.Router();  

// 모든 유저 정보를 제공하는 라우팅
router.get('/', function (req, res, next) {
  res.json(users);
});

// 경로 매개변수를 사용한 라우팅: 특정 유저 정보 제공
router.get('/:id', function (req, res, next) {
  user = users.find(u => u.id === parseInt(req.params.id))
  res.send(user);
});

// POST
router.post('/', function (req, res, next) {
  console.log(req.body)
  const raw = {
    X1:parseFloat(req.body.X1),
    X2:parseFloat(req.body.X2),
    X3:parseFloat(req.body.X3)
  }
  // res.send(raw);
  console.log(req.body)
  console.log(raw)
  raw_str = JSON.stringify(raw)
  var options = {
    mode:'text',
    pythonPath:'',
    pythonOptions:['-u'],
    scriptPath:'C:\\Users\\nww73\\Documents\\GitHub\\Web\\testapp\\routes',
    args:raw_str
  }

  PythonShell.run('test.py', options, function (err, results) {
    if (err) throw err;
    console.log(err);
    console.log('results: %j', results);
    res.send(results);
  });
});

module.exports = router;