(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-25dec777"],{c26b1:function(t,o,n){"use strict";n("e448")},e448:function(t,o,n){},f4a0:function(t,o,n){"use strict";n.r(o);var e=function(){var t=this,o=t._self._c;return o("div",{staticClass:"loading"},[o("SimpleModalDlg",{attrs:{modalId:t.alertModalId,title:t.alertTitle,content:t.alertConent,defaultButtonText:"确认",defaultButtonAction:t.gotoLogin}})],1)},a=[],l=n("fa7d"),i=n("0be2"),c=n("f953"),s=n("5f87"),d="login",u={components:{},data:function(){return{alertModalId:l["a"].randomId("modal"),alertTitle:"",alertConent:""}},methods:{gotoLogin:function(){Object(s["c"])(),this.$router.push({name:d})},showAlert:function(t,o){this.alertTitle=t,this.alertConent=o,c["a"].show(this.alertModalId)},loadSystemInfo:function(){var t="system/systeminfos/";i["a"].apiAjaxGet(t,{},(function(t){0===t.code&&t.data.length>0&&Object(s["l"])(t.data[0])}),l["a"].defaultApiErrorHandler(t,""))},loadAuthInfo:function(){var t=this,o="system/projectinfos/auth_info/";i["a"].apiAjaxGet(o,{},(function(o){0===o.code?(Object(s["k"])(o.data),t.$router.push({name:t.$config.homeName})):t.showAlert("获取设备信息失败","".concat(o.code,": ").concat(o.message,"。"))}),(function(){t.showAlert("获取设备信息失败","获取项目信息失败，请检查网络连接是否正常！")}))}},mounted:function(){this.loadAuthInfo(),this.loadSystemInfo(),Object(s["j"])()}},r=u,f=(n("c26b1"),n("2877")),h=Object(f["a"])(r,e,a,!1,null,null,null);o["default"]=h.exports}}]);