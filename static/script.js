document.querySelector("#show-login").addEventListener("click",function(){
    document.querySelector(".loginpage").classList.toggle("active");
    if(document.querySelector(".registerpage").classList.contains("active"))
    document.querySelector(".registerpage").classList.remove("active");
  });
  document.querySelector(".popup .close-btn").addEventListener("click",function(){
    document.querySelector(".loginpage").classList.remove("active");
  });

document.querySelector('#show-register').addEventListener("click",function() {
    document.querySelector(".registerpage").classList.toggle("active");
    if(document.querySelector(".loginpage").classList.contains("active"))
    document.querySelector(".loginpage").classList.remove("active");
});
document.querySelector(".registerpage .close-btn").addEventListener("click",function(){
    document.querySelector(".registerpage").classList.remove("active");
  });


