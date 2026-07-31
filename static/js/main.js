const jobRadios=document.querySelectorAll("input[name='job_method']");
const resumeRadios=document.querySelectorAll("input[name='resume_method']");

const jobPaste=document.getElementById("jobPaste");
const jobFile=document.getElementById("jobFile");

const resumePaste=document.getElementById("resumePaste");
const resumeFile=document.getElementById("resumeFile");

jobRadios.forEach(r=>{

r.addEventListener("change",()=>{

jobPaste.style.display=r.value==="paste"?"block":"none";
jobFile.style.display=r.value==="paste"?"none":"block";

});

});

resumeRadios.forEach(r=>{

r.addEventListener("change",()=>{

resumePaste.style.display=r.value==="paste"?"block":"none";
resumeFile.style.display=r.value==="paste"?"none":"block";

});

});

const jobUpload=document.getElementById("jobUpload");

if(jobUpload){

jobUpload.addEventListener("change",()=>{

document.getElementById("jobFileName").innerHTML=jobUpload.files[0].name;

});

}

const resumeUpload=document.getElementById("resumeUpload");

if(resumeUpload){

resumeUpload.addEventListener("change",()=>{

document.getElementById("resumeFileName").innerHTML=resumeUpload.files[0].name;

});

}