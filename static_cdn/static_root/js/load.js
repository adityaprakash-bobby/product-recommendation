(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
module.exports = function(opts) {
  var clientId, currencyCode, image, labelId;
  labelId = (opts != null ? opts.labelId : void 0) || 'mKFLCMfduJYBEIe6lcsD';
  currencyCode = (opts != null ? opts.currencyCode : void 0) || 'USD';
  clientId = (opts != null ? opts.clientId : void 0) || '962944263';
  image = new Image(0, 0);
  image.id = 'p13n-mb-pixel';
  image.src = "//www.googleadservices.com/pagead/conversion/" + clientId + "/?value=1.00&currency_code=" + currencyCode + "&gclaw=GCLID1.GCLID2.GCLID3&label=" + labelId + "&guid=ON&script=0";
  document.getElementsByTagName("body")[0].appendChild(image);
};


},{}],2:[function(require,module,exports){
module.exports = function(src, cb) {
  var script;
  script = document.createElement("script");
  script.type = "text/javascript";
  script.src = src;
  if (typeof cb === "function") {
    script.addEventListener('load', cb, false);
  }
  document.getElementsByTagName("head")[0].appendChild(script);
};


},{}],3:[function(require,module,exports){
var AddPixelTracking, date, getCookie, setCookie, setupCampaign, url;

require('./styles.less');

if (window.p13nAddScriptWithCb == null) {
  window.p13nAddScriptWithCb = require('./addScript');
}

AddPixelTracking = require('./addPixel');

date = new Date();

date.setDate(date.getDate() + 21);

url = typeof testUrl !== "undefined" && testUrl !== null ? testUrl : window.location.href;

setCookie = function(name, val, opts) {
  var cookie;
  cookie = void 0;
  cookie = name + '=' + val;
  if (opts) {
    if (opts.expDate) {
      cookie += '; expires=' + opts.expDate.toGMTString();
    }
    if (opts.path) {
      cookie += '; path=' + escape(opts.path);
    }
    if (opts.domain) {
      cookie += '; domain=' + escape(opts.domain);
    }
    if (opts.secure) {
      cookie += '; secure';
    }
  }
  return document.cookie = cookie;
};

getCookie = function(name) {
  var c, ca, i, len, nameEq;
  c = void 0;
  ca = void 0;
  i = void 0;
  len = void 0;
  nameEq = void 0;
  nameEq = name + '=';
  ca = document.cookie.split(';');
  i = 0;
  len = ca.length;
  while (i < len) {
    c = ca[i];
    while (c.charAt(0) === ' ') {
      c = c.substring(1, c.length);
    }
    if (c.indexOf(nameEq) === 0) {
      return c.substring(nameEq.length, c.length);
    }
    i++;
  }
  return null;
};

setupCampaign = function() {
  var campaign, campaignLibrary, setExperience, setMbMessage;
  campaignLibrary = window.p13nTargetCampaignLibrary;
  campaign = new campaignLibrary.ABCampaign({
    name: "campaign-mb",
    showLogs: true
  });
  campaign.log("[" + campaign.name + "] campaign set up");
  if (url.indexOf('ref=mb') !== -1) {
    setCookie('mb', true, {
      expDate: date,
      path: '/',
      domain: document.domain
    });
  }
  setMbMessage = function() {
    var message;
    message = '<div id="mb-message"><h4>Why register for Dell Premier Solutions?</h4><div><p>Dell Premier Solutions are the most proficient way to procure the technologies you need to run your business - directly from Dell and Dell Partners - while improving process, manageability and efficiency.</p><ul><li>Set company-wide standards for product configurations, custom services and shipping options and purchase at your organization&apos;s negotiated rate.</li><li>Retrieve detailed invoice, open order and purchase history reports or build your own report.</li><li>Prepare and save system configurations as an eQuote for repeat or future purchases at a later date.</li></ul></div> <a target="_blank" href="https://www.dellemc.com/en-us/premier-solutions/get-started.htm" class="btn btn-primary p13n-premier-link">Sign Up for Premier</a><a class="mb-learnmore" href="//www.dell.com/premiersolutions">Learn More</a></div>';
    $('#faq-links').parent('div').prepend(message);
    return $('.create-account-with-email').hide();
  };
  setExperience = function() {
    var mbCookie;
    mbCookie = getCookie('mb');
    if (mbCookie === 'true') {
      $('#message-bar,#messagebar').hide();
      $('<div id="mb-site-message"><div class="container"><div class="col-md-12 col-xs-10 p13n-container"><div class="p13n-image hidden-xs hidden-sm"><img src="//i.dell.com/sites/csimages/Merchandizing_Imagery/all/new-lati-opti-group-site-search-165x119.png" class="img-responsive"></div><div class="p13n-line">Dell Mid-Market Solutions: Save 38% instantly on select Latitude and OptiPlex PCs<div><a href="//www.dell.com/en-us/work/shop/deals/mbdeals/mid-market-deals">Shop Now</a></div></div></div></div></div>').insertAfter(".navbar,#cf-masthead");
      $("[class*=contact-drawer]").remove();
      $('.smalldevices-chat-icon').remove();
      if ($(".backToRoot:visible").length !== 0) {
        $(".backToRoot").trigger('click.rootCategory');
      }
      if (url.indexOf('confirmation') > 0) {
        setMbMessage();
        return AddPixelTracking();
      }
    }
  };
  campaign.start = function() {
    campaign.log("[" + campaign.name + "] campaign started");
    return setExperience();
  };
  return campaign.init();
};

if (!(Dell.Metrics.sc.pagename.match(/(shop\|home|homepage)/ig) && !Dell.Metrics.sc.pagename.match(/^us\|en\|bsd\|04\|stp\|/ig))) {
  if (!(typeof window.p13nTargetCampaignLibrary !== 'undefined')) {
    window.p13nAddScriptWithCb("https://p.cdn.persaas.dell.com/p13n/tools/target-campaign-library-1.1.js", function() {
      return setupCampaign();
    });
  } else {
    setupCampaign();
  }
}


},{"./addPixel":1,"./addScript":2,"./styles.less":4}],4:[function(require,module,exports){
(function() { var head = document.getElementsByTagName('head')[0]; var style = document.createElement('style'); style.type = 'text/css';var css = "@media (max-width:767px){.masthead-visible-in-offcanvas-view-with-masthead-labels.affix-active #mb-site-message{display:none}}#mb-site-message{color:#444;background-color:#eee;border-bottom:1px solid #ddd}#mb-site-message .container{text-align:left;padding-top:0;padding-bottom:0}#mb-site-message .p13n-container{font-size:14px;line-height:20px;padding:4px;padding-left:15px;padding-right:30px;-webkit-justify-content:flex-start;-ms-flex-pack:start;justify-content:flex-start;-webkit-box-align:center;-webkit-align-items:center;-webkit-box-flex:1;-webkit-flex:1;-ms-flex:1;flex:1;display:-webkit-box;display:-ms-flexbox}#mb-site-message .p13n-container .p13n-line{display:block}#mb-site-message .p13n-container .p13n-image .img-responsive{max-height:40px;width:auto;padding-right:8px}@media (max-width:991px){#mb-site-message .p13n-container{font-size:12px;line-height:16px}}#mb-message{border:1px solid #ccc;background:#f9f9f9;margin:5px 0 20px;padding:20px}#mb-message .container{text-align:left;font-size:14px;padding:10px 20px}#mb-message .p13n-premier-link{display:inline-block;margin:15px 0 0;width:145px}#mb-message .mb-learnmore{display:inline-block;vertical-align:top;margin:22px 0 0 20px}#mb-message h4{color:#444}";if (style.styleSheet){ style.styleSheet.cssText = css; } else { style.appendChild(document.createTextNode(css)); } head.appendChild(style);}())
},{}]},{},[3]);
