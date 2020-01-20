// autofill for file names as user enters will be added using the inquirer package
#!/usr/bin/env node --harmony

const 
  inquirer = require('inquirer');

  fs = require('fs');
// prompt will be changed to a number:value pair instead of string
inquirer.prompt([
    {
      type:'list',
      name: 'operations',
      message: 'Choose a file operation',
      choices: ['create', 'read', 'write', 'delete', 'copy'],
},
])
.then(async (answers) => {
    var toDo = answers.operations;
   console.log(toDo);
   if(toDo == 'create')
    {
       console.log(toDo);
       createFunc();
    }
   else if(toDo == 'read')
    {
      console.log(toDo);
      readFunc();
    
    }
   else if(toDo == 'write')
   {
     console.log(toDo);
     writeFunc();
 
   }
   else if(toDo == 'delete')
   {
    console.log(toDo);
    deleteFunc();
 }
  else if(toDo == 'copy')
  {
   console.log(toDo);
   copyFunc();
   } 
  
});

function createFunc()
{
  inquirer.prompt([
     {
        name:'createFileValue1',
        message: 'enter the file path',
        default: '.',
     },
     {
       name:'createFileValue2',
       message: 'enter the file name',
     },

  ])
  .then(answers => {
     var filepath = answers.createFileValue1;
     var filename = answers.createFileValue2;       
  
    file = filepath + '/' + filename;

fs.access(filepath, fs.constants.X_OK, (err) => {
  if(err)
  {
    console.log("not enough permissions");
  }

else {

console.log("Permitted to proceed further!!");

fs.open(file, 'r', function(err,data){
  if(err)
  {
    fs.writeFile(file, '', function(err){
       if(err){
          console.log(err);
       }
      console.log("saved the new file");

   });
  }
 else
  {

    console.log("file already exists!!");
  }

});


}
});
});
}

function readFunc()
{
  inquirer.prompt([
     {
        name:'createFileValue1',
        message: 'enter the file path',
        default: '.',
     },
     {
       name:'createFileValue2',
       message: 'enter the file name',
     },

  ])
  .then(answers => {
     var filepath = answers.createFileValue1;
     var filename = answers.createFileValue2; 
     file = filepath + '/' + filename; 
    stream = fs.createReadStream(file);


fs.access(file, fs.constants.R_OK, (err) =>{
 if(err)
{
  console.log("not enough permissions");
}

else
{
  console.log("permission to proceed further!!");

stream.on('data', function(chunk){
  process.stdout.write(chunk);
});
stream.on('error',function(err){
  process.stderr.write("ERROR:" + err.message + "\n");
});
}
});

});
}

function writeFunc()
{
 inquirer.prompt([
     {
        name:'createFileValue1',
        message: 'enter the file path',
        default: '.',
     },
     {
       name:'createFileValue2',
       message: 'enter the file name',
     },
    { 
       name: 'createFileValue3',
       message: 'enter the data to overwrite',

    },
     

  ])
  .then(answers => {
     var filepath = answers.createFileValue1;
     var filename = answers.createFileValue2;
     var newData = answers.createFileValue3;

     var file = filepath + '/' + filename;
     stream = fs.createWriteStream(file);

fs.access(file, fs.constants.W_OK , (err) => {
  if(err)
  {
   console.log("not enough permission..");
  }
  else
  {

    console.log("permission to proceed further!!");

    stream.write(newData);
    stream.on('error', function(err) {
    process.stderr.write("ERROR:" + err.message + "\n");

});
}
});
});
}

function deleteFunc()
{

inquirer.prompt([
     {
        name:'createFileValue1',
        message: 'enter the file path',
        default: '.',
     },
     {
       name:'createFileValue2',
       message: 'enter the file name',
     },
  ])
  .then(answers => 
{
     var filepath = answers.createFileValue1;
     var filename = answers.createFileValue2;
     file = filepath + '/' + filename;
     


fs.access(filepath, fs.constants.X_OK, (err) => {
  if(err)
  {
    console.log("not enough permissions");
  }

else {

console.log("Permitted to proceed further!!");
fs.unlink(file, (err) =>{
  if(err){
    console.log(err);
  }

});

}
});
});
}

function copyFunc()

{
inquirer.prompt([
     {
        name:'createFileValue1',
        message: 'enter the file path',
        default: '.',
     },
     {
       name:'createFileValue2',
       message: 'enter the file name',
     },
     {
       name: 'copyFileDest1',
       message: 'eneter the file path',
       default: '.'
     },
     {
       name: 'copyFileDest2',
       message: 'enter the file name', 
     },
  ])
  .then(answers =>
{
     var filepath = answers.createFileValue1;
     var filename = answers.createFileValue2;
     var destFileName = answers.copyFileDest2;
     var destFilePath = answers.copyFileDest1;
     file = filepath + '/' + filename;
     destFile = destFilePath + '/' + destFileName;


fs.access(filepath, fs.constants.X_OK, (err) => {
  if(err)
  {
    console.log("not enough permissions");
  }

else {

console.log("Permitted to proceed further!!");
fs.copyFile(file, destFile,  (err) =>{
  if(err){
    console.log(err);
  }
  console.log('file successfully copied');

});

}
});
});

}

