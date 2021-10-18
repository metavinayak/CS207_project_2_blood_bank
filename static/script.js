
document.querySelector("#show-login").addEventListener("click",function(){
    document.querySelector(".loginpage").classList.add("active");
  });
  document.querySelector(".popup .close-btn").addEventListener("click",function(){
    document.querySelector(".loginpage").classList.remove("active");
  });

document.querySelector('#show-register').addEventListener("click",function() {
    document.querySelector(".registerpage").classList.add("active");
});
document.querySelector(".registerpage .close-btn").addEventListener("click",function(){
    document.querySelector(".registerpage").classList.remove("active");
  });