(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-774e9bb4"],{"386d":function(t,e,a){"use strict";var n=a("cb7c"),o=a("83a1"),i=a("5f1b");a("214f")("search",1,(function(t,e,a,r){return[function(a){var n=t(this),o=void 0==a?void 0:a[e];return void 0!==o?o.call(a,n):new RegExp(a)[e](String(n))},function(t){var e=r(a,t,this);if(e.done)return e.value;var s=n(t),u=String(this),c=s.lastIndex;o(c,0)||(s.lastIndex=0);var l=i(s,u);return o(s.lastIndex,c)||(s.lastIndex=c),null===l?-1:l.index}]}))},"3b2b":function(t,e,a){var n=a("7726"),o=a("5dbc"),i=a("86cc").f,r=a("9093").f,s=a("aae3"),u=a("0bfb"),c=n.RegExp,l=c,d=c.prototype,m=/a/g,p=/a/g,f=new c(m)!==m;if(a("9e1e")&&(!f||a("79e5")((function(){return p[a("2b4c")("match")]=!1,c(m)!=m||c(p)==p||"/a/i"!=c(m,"i")})))){c=function(t,e){var a=this instanceof c,n=s(t),i=void 0===e;return!a&&n&&t.constructor===c&&i?t:o(f?new l(n&&!i?t.source:t,e):l((n=t instanceof c)?t.source:t,n&&i?u.call(t):e),a?this:d,c)};for(var h=function(t){t in c||i(c,t,{configurable:!0,get:function(){return l[t]},set:function(e){l[t]=e}})},g=r(l),v=0;g.length>v;)h(g[v++]);d.constructor=c,c.prototype=d,a("2aba")(n,"RegExp",c)}a("7a56")("RegExp")},8287:function(t,e,a){"use strict";a("c377")},"83a1":function(t,e){t.exports=Object.is||function(t,e){return t===e?0!==t||1/t===1/e:t!=t&&e!=e}},c377:function(t,e,a){},e49c:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t._self._c;return e("div",{staticClass:"login"},[e("div",{staticClass:"login-con"},[e("Card",{attrs:{icon:"log-in",title:"欢迎登录",bordered:!1}},[e("div",{staticClass:"form-con"},[e("login-form",{on:{"on-success-valid":t.handleSubmit,"on-activate-again":t.activateAgain}})],1)])],1),e("ActivateDlg",{attrs:{modalId:t.authModalId},on:{"auth-success":t.authSuccess,"auth-failed":t.authFailed}})],1)},o=[],i=function(){var t=this,e=t._self._c;return e("Form",{ref:"loginForm",attrs:{model:t.form,rules:t.rules},nativeOn:{keydown:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.handleSubmit.apply(null,arguments)}}},[e("FormItem",{attrs:{prop:"userName"}},[e("Input",{attrs:{placeholder:"请输入用户名"},model:{value:t.form.userName,callback:function(e){t.$set(t.form,"userName",e)},expression:"form.userName"}},[e("span",{attrs:{slot:"prepend"},slot:"prepend"},[e("Icon",{attrs:{size:16,type:"ios-person"}})],1)])],1),e("FormItem",{attrs:{prop:"password"}},[e("Input",{attrs:{type:"password",placeholder:"请输入密码"},model:{value:t.form.password,callback:function(e){t.$set(t.form,"password",e)},expression:"form.password"}},[e("span",{attrs:{slot:"prepend"},slot:"prepend"},[e("Icon",{attrs:{size:14,type:"md-lock"}})],1)])],1),e("FormItem",[e("Button",{attrs:{type:"primary",long:""},on:{click:t.handleSubmit}},[t._v("登录")])],1),e("FormItem",[e("Button",{attrs:{type:"primary",long:""},on:{click:t.activateAgain}},[t._v("激活 / 重新激活")])],1)],1)},r=[],s={name:"LoginForm",props:{userNameRules:{type:Array,default:function(){return[{required:!0,message:"账号不能为空",trigger:"blur"}]}},passwordRules:{type:Array,default:function(){return[{required:!0,message:"密码不能为空",trigger:"blur"}]}}},data:function(){return{form:{userName:"super_admin",password:""}}},computed:{rules:function(){return{userName:this.userNameRules,password:this.passwordRules}}},methods:{handleSubmit:function(){var t=this;this.$refs.loginForm.validate((function(e){e&&t.$emit("on-success-valid",{userName:t.form.userName,password:t.form.password})}))},activateAgain:function(){this.$emit("on-activate-again")}}},u=s,c=a("2877"),l=Object(c["a"])(u,i,r,!1,null,null,null),d=l.exports,m=d,p=function(){var t=this,e=t._self._c;return e("SimpleModalDlg",{attrs:{modalId:t.modalId,title:"系统激活",content:"",defaultButtonText:"取消",button2Text:"激活",button2Action:t.button2Action,dialogWidth:600,showClose:!1},scopedSlots:t._u([{key:"bodyPost",fn:function(){return[e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[e("div",{staticClass:"col-4"},[e("span",{staticClass:"field-label"},[t._v("项目名称：")])]),e("div",{staticClass:"col mb-1"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.projectName,expression:"projectName"}],staticClass:"mr-1",staticStyle:{width:"20em"},domProps:{value:t.projectName},on:{input:function(e){e.target.composing||(t.projectName=e.target.value)}}}),e("IconFont",{class:t.projectNameValid?"dagou-icon":"dacha-icon",attrs:{iconName:t.projectNameValid?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}})],1),e("div",{staticClass:"col-4"},[e("span",{staticClass:"field-label"},[t._v("授权码：")])]),e("div",{staticClass:"col mb-1"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.authCode,expression:"authCode"}],staticClass:"mr-1",staticStyle:{width:"20em"},domProps:{value:t.authCode},on:{input:function(e){e.target.composing||(t.authCode=e.target.value)}}}),e("IconFont",{class:t.authCodeValid?"dagou-icon":"dacha-icon",attrs:{iconName:t.authCodeValid?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}})],1),e("div",{staticClass:"col-4"},[e("span",{staticClass:"field-label"},[t._v("用户名：")])]),e("div",{staticClass:"col mb-1"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.username,expression:"username"}],staticClass:"mr-1",staticStyle:{width:"20em"},domProps:{value:t.username},on:{input:function(e){e.target.composing||(t.username=e.target.value)}}}),e("IconFont",{class:t.usernameValid?"dagou-icon":"dacha-icon",attrs:{iconName:t.usernameValid?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}})],1)]),e("div",{staticClass:"row mb-1"},[e("div",{staticClass:"col-4"},[e("span",{staticClass:"field-label"},[t._v("密码：")])]),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.password1,expression:"password1"}],staticClass:"mr-1",staticStyle:{width:"20em"},attrs:{type:"password"},domProps:{value:t.password1},on:{input:function(e){e.target.composing||(t.password1=e.target.value)}}}),e("IconFont",{class:t.password1Valid?"dagou-icon":"dacha-icon",attrs:{iconName:t.password1Valid?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}})],1)]),e("div",{staticClass:"row mb-1"},[e("div",{staticClass:"col-4"},[e("span",{staticClass:"field-label"},[t._v("密码(再次输入)：")])]),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.password2,expression:"password2"}],staticClass:"mr-1",staticStyle:{width:"20em"},attrs:{type:"password"},domProps:{value:t.password2},on:{input:function(e){e.target.composing||(t.password2=e.target.value)}}}),e("IconFont",{class:t.password2Valid?"dagou-icon":"dacha-icon",attrs:{iconName:t.password2Valid?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}})],1)])])]},proxy:!0}])})},f=[],h=a("fa7d"),g=a("f953"),v=a("0be2"),b={name:"ActivateDlg",components:{SimpleModalDlg:g["a"]},data:function(){return{username:"",password1:"",password2:"",projectName:"",authCode:""}},props:{modalId:{type:String,required:!0}},computed:{projectNameValid:function(){return this.projectName.trim().length>0},authCodeValid:function(){return 32===this.authCode.trim().length},usernameValid:function(){return this.username.trim().length>0},password1Valid:function(){return this.password1.length>=6},password2Valid:function(){return this.password2.length>=6&&this.password1===this.password2}},methods:{authFailed:function(){return this.$emit("auth-failed"),0},button2Action:function(){var t=this,e="system/projectinfos/activate/",a={};return this.projectNameValid?(a["project_name"]=this.projectName.trim(),this.authCodeValid?(a["auth_code"]=this.authCode.trim(),this.usernameValid?(a["username"]=this.username.trim(),this.password1!==this.password2?(alert("两次密码输入必须一致！"),this.authFailed()):this.password1Valid?(a["password"]=this.password1,void v["a"].apiAjaxPost(e,a,(function(e){if(console.log("Activate return",e),0!==e.code)return alert("激活失败(".concat(e.code,"): ").concat(e.message)),t.authFailed();alert("激活成功！"),t.$emit("auth-success")}),(function(){return t.authFailed()}))):(alert("密码太短！"),this.authFailed())):(alert("用户名不能为空！"),this.authFailed())):(alert("授权码不能为空！"),this.authFailed())):(alert("项目名称不能为空！"),this.authFailed())}},watch:{},mounted:function(){}},y=b,w=Object(c["a"])(y,p,f,!1,null,null,null),C=w.exports,x=a("5f87"),_={components:{LoginForm:m,ActivateDlg:C},data:function(){return{authModalId:h["a"].randomId("modalId")}},methods:{authFailed:function(){var t=this;setTimeout((function(){$("#".concat(t.authModalId)).modal("show")}),500)},authSuccess:function(){var t=this,e="system/projectinfos/auth_info/";v["a"].apiAjaxGet(e,{},(function(e){0===e.code&&e.data?Object(x["g"])(e.data):(alert("激活失败，请确认授权码有效！"),$("#".concat(t.authModalId)).modal("show"))}),h["a"].defaultApiErrorHandler(e,""))},handleSubmit:function(t){var e=this,a=t.userName,n=t.password,o="api-token-auth/";v["a"].apiAjaxPost(o,{username:a,password:n},(function(t){"token"in t?(Object(x["j"])(a),Object(x["h"])(t["token"]),Object(x["i"])(t["token"],{access:["super_admin","admin"]}),e.$emit("login-success"),e.$router.push({name:e.$config.homeName})):alert("用户名或密码错误！")}),h["a"].defaultApiErrorHandler(o,""))},activateAgain:function(){$("#".concat(this.authModalId)).modal("show")}},mounted:function(){var t=this;Object(x["c"])()||setTimeout((function(){$("#".concat(t.authModalId)).modal("show")}),1e3)}},I=_,N=(a("8287"),Object(c["a"])(I,n,o,!1,null,null,null));e["default"]=N.exports},f953:function(t,e,a){"use strict";var n=function(){var t=this,e=t._self._c;return e("ModalDlgFrame",{attrs:{modalId:t.modalId,dialogWidth:t.dialogWidth,titleBg:t.titleBg,showClose:t.showClose},scopedSlots:t._u([{key:"title",fn:function(){return[t._v("\n    "+t._s(t.title)+"\n  ")]},proxy:!0},{key:"body",fn:function(){return[t._t("bodyPre"),t.content.length>0?e("pre",{staticClass:"text-left"},[t._v(t._s(t.content))]):t._e(),t._t("bodyPost")]},proxy:!0},{key:"footer",fn:function(){return[t._t("footerPre"),e("button",{directives:[{name:"show",rawName:"v-show",value:!!t.defaultButtonText,expression:"!!defaultButtonText"}],staticClass:"btn btn-default btn-primary",attrs:{type:"button","data-dismiss":"modal"},on:{click:t.defaultButtonAction}},[t._v("\n      "+t._s(t.defaultButtonText)+"\n    ")]),t.button2Text?e("button",{staticClass:"btn btn-outline-primary",attrs:{type:"button","data-dismiss":"modal"},on:{click:t.button2Action}},[t._v("\n      "+t._s(t.button2Text)+"\n    ")]):t._e(),t.button3Text?e("button",{staticClass:"btn btn-outline-primary",attrs:{type:"button","data-dismiss":"modal"},on:{click:t.button3Action}},[t._v("\n      "+t._s(t.button3Text)+"\n    ")]):t._e(),t._t("footerPost")]},proxy:!0}],null,!0)})},o=[],i=(a("c5f6"),function(){var t=this,e=t._self._c;return e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"modal fade modal-open",attrs:{"data-backdrop":"static",id:t.modalId,tabindex:"-1",role:"dialog"}},[e("div",{staticClass:"modal-dialog draggable align-self-center",attrs:{role:"document"}},[e("div",{staticClass:"modal-content",style:t.contentStyle},[e("div",{class:"modal-header panel-heading py-0 "+t.titleBg},[e("h5",{staticClass:"modal-title"},[t._t("title")],2),t.showClose?e("button",{staticClass:"close",attrs:{type:"button","data-dismiss":"modal","aria-label":"Close"}},[e("span",{attrs:{"aria-hidden":"true"}},[t._v("×")])]):t._e()]),e("div",{staticClass:"modal-body"},[t._t("body")],2),e("div",{staticClass:"modal-footer"},[t._t("footer")],2)])])])])}),r=[],s=a("1157"),u=a.n(s),c={name:"ModalDlgFrame",props:{modalId:{type:String,required:!0},titleBg:{type:String,required:!1,default:"bg-primary"},dialogWidth:{type:Number,required:!1,default:800},showClose:{type:Boolean,required:!1,default:!0}},data:function(){return{}},methods:{modalCenter:function(){var t=u()("#".concat(this.modalId," ")+".modal-dialog");if(t.is(":visible")){u()("#".concat(this.modalId)).css("display","block");var e=u()("#".concat(this.modalId," ")+".modal-content"),a=e.outerHeight(!0),n=e.outerWidth(!0),o=u()(window).height()/2-a/2;o<10&&(o=10),t.css("margin-top",o+"px");var i=u()(window).width()/2-n/2;t.css("margin-left",i+"px")}}},computed:{contentStyle:function(){return{width:this.dialogWidth+"px"}}},created:function(){},mounted:function(){u()("#".concat(this.modalId)).on("shown.bs.modal",this.modalCenter),u()(window).on("resize",this.modalCenter)}},l=c,d=a("2877"),m=Object(d["a"])(l,i,r,!1,null,"cba0f672",null),p=m.exports,f={name:"SimpleModalDlg",components:{ModalDlgFrame:p},data:function(){return{}},props:{modalId:{type:String,required:!0},titleBg:{type:String,required:!1,default:"bg-primary"},defaultButtonText:{type:String,required:!1,default:"Close"},defaultButtonAction:{type:Function,required:!1,default:function(){}},button2Text:{type:String,required:!1,default:""},button2Action:{type:Function,required:!1,default:function(){}},button3Text:{type:String,required:!1,default:""},button3Action:{type:Function,required:!1,default:function(){}},title:{type:String,required:!1,default:"Simple Dialog"},content:{type:String,required:!1,default:""},dialogWidth:{type:Number,required:!1,default:600},showClose:{type:Boolean,required:!1,default:!0}},mounted:function(){}},h=f,g=Object(d["a"])(h,n,o,!1,null,null,null);e["a"]=g.exports},fa7d:function(t,e,a){"use strict";a("456d"),a("ac6a");var n=a("53ca");a("7514"),a("28a5"),a("a481"),a("3b2b"),a("386d");e["a"]={nextTableSelectedIndex:function(t,e){var a=e+1;while(a<t.length){if(t[a].selected)break;a++}return a},downloadFile:function(t){var e=document.createElement("iframe");e.style.display="none",e.style.height=0,e.src=t,document.body.appendChild(e),setTimeout((function(){e.remove()}),3e5)},randomString:function(t){for(var e=t||8,a="ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678",n=a.length,o="",i=0;i<e;i++)o+=a.charAt(Math.floor(Math.random()*n));return o},randomId:function(t){return"".concat(t,"-").concat(this.randomString())},getProtocolHostPort:function(){var t=document.location.protocol;":"===!t.substr(t.length-1,1)&&(t+=":");var e=document.location.host;return e.search(":"+document.location.port)<0&&(e+=":"+document.location.port),"".concat(t,"//").concat(e)},getThumbPathPrefix:function(){return"".concat(this.getProtocolHostPort(),"/nc19api/v1/fileservice/images/")},getThumbPathPostfix:function(t){return"thumb/?thumb_size=".concat(t,"&id=")},replaceChinese:function(t){var e={"：":":","，":",","；":";","？":"?","‘":"'","’":"'","“":'"',"”":'"',"！":"!","＃":"#","＆":"&","×":"*","（":"(","）":")","－":"-","—":"_","＋":"+","＝":"=","｛":"{","｝":"}","【":"[","】":"]","｜":"|","～":"~","《":"<","》":">","​":"","＞":">","＜":"<","★":"*","。":". ","、":"\\","∽":"~","￠":"","":"","氧传感":"Oxygen Sensor","(盎司)":"(ounces)","．":". "};for(var a in e){var n=new RegExp(a,"g");t=t.replace(n,e[a])}return t},filterEnglishOrSymbol:function(t){return t&&t.search(/[\u4e00-\u9fa5]/)>=0?"Chinese Characters":""},getProductEditUrl:function(t,e,a,n,o){var i=t.$router.resolve({path:"/products/products/productedit",query:{product_id:e,source:a,auto_save:n?1:0,view_only:o?1:0}});return i},openProductEditPageEx:function(t,e,a,n){var o=this.getProductEditUrl(t,e,a,n);window.open(o.href,"_blank")},openProductEditPage:function(t,e,a){this.openProductEditPageEx(t,e,a,0)},getDateFromDateTimeString:function(t){return t.split("T")[0]},getImageThumbById:function(t,e,a){var n="".concat(t.img_root,"thumb/?id=").concat(e);return a&&(n="".concat(n,"&thumb_size=").concat(a)),n},getImageThumbByName:function(t,e,a){var n="".concat(t.img_root,"thumb/").concat(e);return a&&(n="".concat(n,"?thumb_size=").concat(a)),n},getImageLinkByName:function(t,e){return"".concat(t.img_root).concat(e)},getLabelFromOptionMap:function(t,e,a,n){var o=t.find((function(t){return t[e]===n}));return o[a]},getDayDiff:function(t,e){return(new Date(t).getTime()-new Date(e))/864e5},defaultApiErrorHandler:function(t,e){return function(a){console.log("".concat(t," failed(").concat(e,"): "),a),"response"in a&&"data"in a.response&&a.response.data instanceof Object&&"data"in a.response.data&&a.response.data.data}},arrayEqual:function(t,e){if(!t||!e)return!t&&!e;if(t.length!==e.length)return!1;for(var a=0;a<t.length;a++)if(t[a]instanceof Array&&e[a]instanceof Array){if(!this.arrayEqual(t[a],e[a]))return!1}else if(t[a]!==e[a])return!1;return!0},deepCopy:function(t){var e=this;if(null===t||"object"!==Object(n["a"])(t))return t;var a=Array.isArray(t)?[]:{};return Object.keys(t).forEach((function(n){a[n]=e.deepCopy(t[n])})),a},eval:function(t){var e=Function;return new e("return "+t)()},getImageUrl:function(t){return"".concat("/static/images","/").concat(t)}}}}]);