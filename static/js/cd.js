var domain = document.location.hostname;
var user = "martin";
var domain = "@" + domain;
var result = user + domain;
document.write('<a href="mailto:' + result + '">' + result + '</a>');
