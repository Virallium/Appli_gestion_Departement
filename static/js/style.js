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
        window.addEventListener("load", ()=>{
        sk.classList.add("removeSkeleton")
    })
})
