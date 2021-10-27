console.log("hello world from js");
/* Get the text field */
var copyTextList = document.querySelectorAll(".copy");
var icopyList = document.querySelectorAll(".icopy");
copyTextList.forEach(copyText => {
  copyText.addEventListener('click',()=>{
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */

    /* Copy the text inside the text field */
    document.execCommand("copy");

    setTimeout(()=>{
      document.getSelection().removeAllRanges();
    },500)

  })
  
});
icopyList.forEach(icopy=>{
  icopy.addEventListener("click",()=>{
    console.log("icopy");
    let father = icopy.parentNode;
    console.log(father)
    father.childNodes
    let theInputField = father.childNodes[2];
    theInputField.select();
    theInputField.setSelectionRange(0, 99999); /* For mobile devices */
    /* Copy the text inside the text field */
    document.execCommand("copy");
    document.getSelection().removeAllRanges();
    icopy.classList.remove("btn-outline-primary");
    icopy.classList.add("btn-outline-success");
    icopy.classList.add("active");
    setTimeout(()=>{
      icopy.classList.remove("btn-outline-success");
      icopy.classList.remove("active");
      icopy.classList.add("btn-outline-primary");
    },500)
  })
})

  
