console.log('Hello from static/blog/js/main.js');

document.addEventListener('DOMContentLoaded',event=>{
    // update current year
    let currentYear = document.querySelector('span.currentYear');
    if (currentYear){
        // get current year
        const nowYear=new Date().getFullYear();
        currentYear.textContent=nowYear;
    }
});