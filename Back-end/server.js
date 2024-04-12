const fs = require('fs')
const path = require('path')

//reading a existing files
fs.readFile(path.join(__dirname,'files','datas.txt'), 'utf-8', (err, data) => {
    if(err) throw err
    console.log(data)
})

//create and update a file
let content = 'New file created'
let updatedContent = '\n updation successfully'
let renameFile = path.join(__dirname, 'files', 'fileOptimized')
fs.writeFile(path.join(__dirname, 'files', 'newFile.txt'), content, (err)=>{
    if(err) throw err
    console.log('File Created Succesfully')
    
    //update the exisiting file
    fs.appendFile(path.join(__dirname, 'files', 'newFile.txt'), updatedContent, (err) =>{
        if(err)throw err
        console.log('Updation completed')

        //rename the exisiting file name
        fs.rename(path.join(__dirname, 'files', 'newFile.txt'), renameFile, (err) => {
            if(err) throw err
            console.log('Rename successfully')
        })
    })
})

//appendFile also create a new file 
let empData = 'id = 102 \n Name = Akshayaa'
fs.appendFile(path.join(__dirname, 'datas', 'employeeData.txt'), empData, (err) =>{
    if(err)
    throw err
    console.log('Appending complete')
})

//catching error
process.on('uncaughtException', err => {
    console.log(err)
    process.exit()
})
