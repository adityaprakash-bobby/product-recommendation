var boxes = [
  {
    selector: ".box:nth-child(2)",
    degree: 45
  },
  {
    selector: ".box:nth-child(3)",
    degree: 30
  },
  {
    selector: ".box:nth-child(4)",
    degree: 60
  }
];

boxes.map(function(box) {
  TweenMax.staggerTo(box.selector, 1, { rotation: box.degree }, 0.2);
});

var tabPills = $(".tab-pills li");
var signUpContent = $("#signup");
var signInContent = $("#signin");
var signInTab = $("#tab-signin");
var signUpTab = $("#tab-signup");

tabPills.click(function(e) {
  var targetTab = e.target.dataset.tab;
  switch (targetTab) {
    case "signin":
      signInTab.addClass("active");
      signInContent.removeClass("hidden-content");
      signInContent.addClass("active-content");
      signUpTab.removeClass("active");
      signUpContent.addClass("hidden-content");
      break;
    case "signup":
      signUpTab.addClass("active");
      signUpContent.removeClass("hidden-content");
      signUpContent.addClass("active-content");
      signInTab.removeClass("active");
      signInContent.addClass("hidden-content");
      break;
  }
});
