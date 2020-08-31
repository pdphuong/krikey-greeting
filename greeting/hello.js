var restify = require('restify');
var errs = require('restify-errors')

function respond(req, res, next) {

  if (!('name' in req.query)) {
    next(new errs.BadRequestError('\'name\' query parameter is missing'))
  }else {
    res.contentType = 'json'  
    res.send({greeting: 'Hello ' + req.query.name});
    next();
  }  
}

var server = restify.createServer();
server.use(restify.plugins.queryParser());
server.get('/greetings', respond);

server.listen(8080, function() {
  console.log('%s listening at %s', server.name, server.url);
});
