(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-b79da050"],{"49ee":function(t,a,s){},"654a":function(t,a,s){},"77c9":function(t,a,s){"use strict";s("49ee")},"7d3e":function(t,a,s){},b3ca:function(t,a,s){"use strict";s("7d3e")},e49c:function(t,a,s){"use strict";s.r(a);var o=function(){var t=this,a=t._self._c;return a("div",{staticClass:"login"},[a("div",{staticClass:"login-con"},[a("Card",{attrs:{icon:"log-in",title:"欢迎登录",bordered:!1}},[a("div",{staticClass:"form-con"},[a("login-form",{on:{"on-success-valid":t.handleSubmit,"on-activate-again":t.activateAgain}})],1)])],1),a("ActivateDlg",{attrs:{modalId:t.authModalId},on:{"auth-success":t.authSuccess,"auth-failed":t.authFailed}}),a("Toast",{attrs:{toastId:t.toastId,text:t.toastText,iconDacha:t.iconDacha}}),a("SimpleModalDlg",{attrs:{modalId:t.alertModalId,content:t.alertConent,defaultButtonText:"确认",defaultButtonAction:t.showAuthModal}})],1)},e=[],i=function(){var t=this,a=t._self._c;return a("Form",{ref:"loginForm",attrs:{model:t.form,rules:t.rules}},[a("FormItem",{attrs:{prop:"userName"}},[a("Input",{attrs:{placeholder:"请输入用户名"},model:{value:t.form.userName,callback:function(a){t.$set(t.form,"userName",a)},expression:"form.userName"}},[a("span",{attrs:{slot:"prepend"},slot:"prepend"},[a("Icon",{attrs:{size:16,type:"ios-person"}})],1)])],1),a("div",{staticClass:"row"},[a("div",{staticClass:"login-blank-row"})]),a("FormItem",{attrs:{prop:"password"}},[a("Input",{attrs:{type:"password",placeholder:"请输入密码"},model:{value:t.form.password,callback:function(a){t.$set(t.form,"password",a)},expression:"form.password"}},[a("span",{attrs:{slot:"prepend"},slot:"prepend"},[a("Icon",{attrs:{size:14,type:"md-lock"}})],1)])],1),a("div",{staticClass:"row"},[a("div",{staticClass:"login-blank-row"})]),a("FormItem",[a("Button",{attrs:{type:"primary",long:""},on:{click:t.handleSubmit}},[t._v("登录")])],1),a("div",{staticClass:"row"},[a("div",{staticClass:"login-blank-row"})]),a("FormItem",[a("Button",{attrs:{type:"primary",long:""},on:{click:t.activateAgain}},[t._v("激活 / 重新激活")])],1)],1)},n=[],r={name:"LoginForm",props:{userNameRules:{type:Array,default:function(){return[{required:!0,message:"账号不能为空",trigger:"blur"}]}},passwordRules:{type:Array,default:function(){return[{required:!0,message:"密码不能为空",trigger:"blur"}]}}},data:function(){return{form:{userName:"",password:""}}},computed:{rules:function(){return{userName:this.userNameRules,password:this.passwordRules}}},methods:{handleSubmit:function(){var t=this;this.$refs.loginForm.validate((function(a){a&&t.$emit("on-success-valid",{userName:t.form.userName,password:t.form.password})}))},activateAgain:function(){this.$emit("on-activate-again")}}},l=r,d=(s("e691"),s("2877")),c=Object(d["a"])(l,i,n,!1,null,null,null),u=c.exports,m=u,p=function(){var t=this,a=t._self._c;return a("SimpleModalDlg",{attrs:{modalId:t.modalId,title:"系统激活",content:"",defaultButtonText:"激活",defaultButtonAction:t.defaultButtonAction,dialogWidth:600,showClose:!1},scopedSlots:t._u([{key:"bodyPost",fn:function(){return[a("div",{staticClass:"container-fluid"},[a("div",{staticClass:"row"},[a("div",{staticClass:"activate-top-blank"})]),a("div",{staticClass:"row text-right"},[a("div",{staticClass:"col-3"},[a("span",{staticClass:"field-label-non-bold"},[t._v("项目名称：")])]),a("div",{staticClass:"col mb-3"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.projectName,expression:"projectName"}],staticClass:"form-control atviation-form-input mr-1",domProps:{value:t.projectName},on:{input:function(a){a.target.composing||(t.projectName=a.target.value)}}})])]),a("div",{staticClass:"row text-right"},[a("div",{staticClass:"col-3"},[a("span",{staticClass:"field-label-non-bold"},[t._v("授权码：")])]),a("div",{staticClass:"col mb-3"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.authCode,expression:"authCode"}],staticClass:"form-control atviation-form-input mr-1",domProps:{value:t.authCode},on:{input:function(a){a.target.composing||(t.authCode=a.target.value)}}})])]),a("div",{staticClass:"row text-right"},[a("div",{staticClass:"col-3"},[a("span",{staticClass:"field-label-non-bold"},[t._v("用户名：")])]),a("div",{staticClass:"col mb-3"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.username,expression:"username"}],staticClass:"form-control atviation-form-input mr-1",domProps:{value:t.username},on:{input:function(a){a.target.composing||(t.username=a.target.value)}}})])]),a("div",{staticClass:"row text-right"},[a("div",{staticClass:"col-3"},[a("span",{staticClass:"field-label-non-bold"},[t._v("密码：")])]),a("div",{staticClass:"col mb-3"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.password1,expression:"password1"}],staticClass:"form-control atviation-form-input mr-1",attrs:{type:"password"},domProps:{value:t.password1},on:{input:function(a){a.target.composing||(t.password1=a.target.value)}}})])]),a("div",{staticClass:"row text-right"},[a("div",{staticClass:"col-3"},[a("span",{staticClass:"field-label-non-bold"},[t._v("密码(再次输入)：")])]),a("div",{staticClass:"col mb-3"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.password2,expression:"password2"}],staticClass:"form-control atviation-form-input mr-1",attrs:{type:"password"},domProps:{value:t.password2},on:{input:function(a){a.target.composing||(t.password2=a.target.value)}}})])]),a("div",{staticClass:"row"},[a("div",{staticClass:"activate-bottom-blank"})])])]},proxy:!0}])})},h=[],f=s("fa7d"),v=s("0be2"),w={name:"ActivateDlg",components:{},data:function(){return{username:"",password1:"",password2:"",projectName:"",authCode:""}},props:{modalId:{type:String,required:!0}},computed:{projectNameValid:function(){return this.projectName.trim().length>0},authCodeValid:function(){return 32===this.authCode.trim().length},usernameValid:function(){return this.username.trim().length>0},password1Valid:function(){return this.password1.length>=6},password2Valid:function(){return this.password2.length>=6&&this.password1===this.password2}},methods:{authFailed:function(t){return this.$emit("auth-failed",t),0},defaultButtonAction:function(){var t=this,a="system/projectinfos/activate/",s={};return this.projectNameValid?(s["project_name"]=this.projectName.trim(),this.authCodeValid?(s["auth_code"]=this.authCode.trim(),this.usernameValid?(s["username"]=this.username.trim(),this.password1!==this.password2?this.authFailed("两次密码输入必须一致！"):this.password1Valid?(s["password"]=this.password1,void v["a"].apiAjaxPost(a,s,(function(a){if(console.log("Activate return",a),0!==a.code)return t.authFailed("激活失败(".concat(a.code,"): ").concat(a.message));t.$emit("auth-success")}),(function(a){return t.authFailed(JSON.stringify(a))}))):this.authFailed("密码太短！")):this.authFailed("用户名不能为空！")):this.authFailed("授权码不能为空！")):this.authFailed("项目名称不能为空！")}},watch:{},mounted:function(){}},g=w,C=(s("77c9"),Object(d["a"])(g,p,h,!1,null,null,null)),b=C.exports,I=s("5f87"),N=s("f953"),x=s("8cbb"),j={components:{LoginForm:m,ActivateDlg:b},data:function(){return{toastId:f["a"].randomId("toast"),authModalId:f["a"].randomId("modal"),alertModalId:f["a"].randomId("modal"),alertConent:"",toastText:"",iconDacha:!0}},methods:{showToast:function(t,a){this.toastText=a,this.iconDacha=t,x["a"].showToast(this.toastId)},authFailed:function(t){var a=this;this.showToast(!0,t),setTimeout((function(){$("#".concat(a.authModalId)).modal("show")}),2500)},showAuthModal:function(){N["a"].show(this.authModalId)},authSuccess:function(){var t=this;this.showToast(!1,"激活成功！"),setTimeout((function(){var a="system/projectinfos/auth_info/";v["a"].apiAjaxGet(a,{},(function(a){0===a.code&&a.data?Object(I["i"])(a.data):t.showToast(!0,"激活失败，请确认授权码有效！")}),f["a"].defaultApiErrorHandler(a,""))}),2500)},handleSubmit:function(t){var a=this,s=t.userName,o=t.password,e="api-token-auth/";v["a"].apiAjaxPost(e,{username:s,password:o},(function(t){"token"in t?(Object(I["l"])(s),Object(I["j"])(t["token"]),Object(I["k"])(t["token"],{access:["super_admin","admin"]}),a.$emit("login-success"),a.$router.push({name:a.$config.homeName})):a.showToast(!0,"用户名或密码错误！")}),f["a"].defaultApiErrorHandler(e,""))},activateAgain:function(){$("#".concat(this.authModalId)).modal("show")}},mounted:function(){var t=this;Object(I["d"])()||setTimeout((function(){$("#".concat(t.authModalId)).modal("show")}),1e3)}},A=j,y=(s("b3ca"),Object(d["a"])(A,o,e,!1,null,null,null));a["default"]=y.exports},e691:function(t,a,s){"use strict";s("654a")}}]);