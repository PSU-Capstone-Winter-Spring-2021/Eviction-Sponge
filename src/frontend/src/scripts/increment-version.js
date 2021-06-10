var _require = require('fs'),
    writeFile = _require.writeFile;

var path = require('path');

var packageJson = require(process.cwd() + "/package.json");

var appVersion = packageJson.version;


let versions = appVersion.split('.')
build = parseInt(versions[2]) + 1
appVersion = versions[0] + '.' + versions[1] + '.' + build.toString()

packageJson.version = appVersion
writeFile(process.cwd() + "/package.json", JSON.stringify(packageJson, null, 2), 'utf8', function (err) {
  if (err) {
    console.error('An error occurred while writing JSON Object to package.json');
    throw console.error(err);
  } else {
    console.log("package.json file has been saved with version: " + appVersion);
  }
});
