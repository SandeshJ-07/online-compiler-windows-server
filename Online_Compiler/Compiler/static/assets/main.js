
// var btn=document.querySelector("#UploadBtn");
// // var Uploadbtn=document.querySelector("#UploadFeild");
// btn.addEventListener('click',()=>{
//     document.querySelector('#upload_profile').click();
// })
document.querySelector('#UploadBtn').addEventListener('click',function(){
    console.log("hello");
    document.querySelector('#UploadFeild').click();
    document.querySelector('#fileform').submit();
  })