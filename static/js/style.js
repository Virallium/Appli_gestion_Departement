const menuIcon = document.getElementById('menu');
const navList = document.querySelector('nav ul');
const rgba=document.querySelector('.rgba');
menuIcon.addEventListener('click', () => {
    navList.classList.toggle('active');
    rgba.classList.toggle('active');
});
rgba.addEventListener('click',()=>{
    navList.classList.remove('active');
    rgba.classList.remove('active');
})
const skeletonAnimation=document.querySelectorAll('.skeleton')
    skeletonAnimation.forEach(sk=>{
        window.addEventListener("DOMContentLoaded", ()=>{
        sk.classList.add("removeSkeleton")
    })
})
const load_anim=document.querySelector('.load_anim')
window.addEventListener('load',() =>{
    load_anim.classList.remove('load_anim')
    load_anim.classList.add('remove_load_anim')
})