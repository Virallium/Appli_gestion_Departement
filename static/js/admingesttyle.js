const btn_ouv=document.querySelector('nav .add')
const btnclose=document.querySelector('#close')
const dialog=document.querySelector('dialog')
btn_ouv.addEventListener('click',()=>{
    dialog.showModal()
    dialog.classList.add('opendialog')
})
btnclose.addEventListener('click',()=>{
    dialog.classList.add('removedialog')
    dialog.close();
})