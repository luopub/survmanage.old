(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0c1b0c"],{"46b6":function(t,e,o){"use strict";o.r(e);var a=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[e("div",{staticClass:"col"},[e("button",{staticClass:"btn btn-primary btn-sm btn-iview-size",attrs:{disabled:t.resetStarted,"data-toggle":"modal","data-target":"#"+t.deviceResetConfirmDlgId}},[t._v(t._s(t.resetStarted?"重启中，请耐心等候...":"重启系统"))])])]),e("div",{staticClass:"row mt-5"},[e("div",{staticClass:"col"},[e("button",{staticClass:"btn btn-primary btn-sm btn-iview-size",attrs:{disabled:t.resetStarted,"data-toggle":"modal","data-target":"#"+t.deviceResetParamsConfirmDlgId}},[t._v(t._s(t.resetStarted?"重启中，请耐心等候...":"重置所有参数"))]),e("br"),e("span",[t._v("注：重置所有参数后，所有设置的参数将会被情况。请谨慎操作！")])])]),e("div",{staticClass:"row mt-5"},[e("div",{staticClass:"col"},[e("button",{staticClass:"btn btn-primary btn-sm btn-iview-size",attrs:{disabled:t.resetStarted,"data-toggle":"modal","data-target":"#"+t.deviceFactoryResetConfirmDlgId}},[t._v(t._s(t.resetStarted?"重启中，请耐心等候...":"恢复出厂设置"))]),e("br"),e("span",[t._v("注：恢复出厂设置后，视频通道将会清空，算法授权将会失效。请谨慎操作！")])])]),e("SystemResetConfirmDlg",{attrs:{modalId:t.deviceResetConfirmDlgId},on:{"reset-started":t.onResetStarted}}),e("SystemResetParamsConfirmDlg",{attrs:{modalId:t.deviceResetParamsConfirmDlgId},on:{"reset-started":t.onResetStarted}}),e("SystemFactoryResetConfirmDlg",{attrs:{modalId:t.deviceFactoryResetConfirmDlgId},on:{"reset-started":t.onResetStarted}}),e("SystemFactoryResetSuccessDlg",{attrs:{modalId:t.deviceFactoryResetSuccessDlgId}})],1)},n=[],s=o("fa7d"),r=function(){var t=this,e=t._self._c;return e("div",[e("SimpleModalDlg",{attrs:{modalId:t.modalId,title:"设备重启",content:"",defaultButtonText:"取消",button2Text:"确认",button2Action:t.button2Action,dialogWidth:500},scopedSlots:t._u([{key:"bodyPost",fn:function(){return[e("IconFont",{staticStyle:{"font-size":"2em",color:"rgb(255, 186, 0)"},attrs:{iconName:"icon-tanhao"}}),t._v("\n    设备重启可能需要几分钟时间。\n  ")]},proxy:!0}])}),e("Toast",{attrs:{toastId:t.toastId,text:"设备重启中"}})],1)},d=[],i=o("f953"),c=o("0be2"),l=o("8cbb"),m={name:"SystemResetConfirmDlg",components:{SimpleModalDlg:i["a"]},data:function(){return{toastId:s["a"].randomId("toast")}},props:{modalId:{type:String,required:!0}},computed:{},methods:{button2Action:function(){var t=this,e="system/projectinfos/reset_device/",o={};c["a"].apiAjaxPost(e,o,(function(){l["a"].showToast(t.toastId),t.$emit("reset-started","restart")}),s["a"].defaultApiErrorHandler(e,""))}},watch:{},mounted:function(){}},u=m,f=o("2877"),p=Object(f["a"])(u,r,d,!1,null,null,null),g=p.exports,b=function(){var t=this,e=t._self._c;return e("div",[e("SimpleModalDlg",{attrs:{modalId:t.modalId,title:"重置所有参数",content:"",defaultButtonText:"取消",button2Text:"确认",button2Action:t.button2Action,dialogWidth:500},scopedSlots:t._u([{key:"bodyPost",fn:function(){return[e("IconFont",{staticStyle:{"font-size":"2em",color:"rgb(255, 186, 0)"},attrs:{iconName:"icon-tanhao"}}),t._v("\n    整个过程大约需要一分钟。所有检测参数将被清除，检测和报警功能将会停止。授权信息、通道信息和历史报警记录将会保留。如果需要开启检测和报警，请重新配置参数。\n  ")]},proxy:!0}])}),e("Toast",{attrs:{toastId:t.toastId,text:"参数已重置，设备重启中"}})],1)},y=[],S={name:"SystemResetParamsConfirmDlg",components:{SimpleModalDlg:i["a"]},data:function(){return{toastId:s["a"].randomId("toast")}},props:{modalId:{type:String,required:!0}},computed:{},methods:{button2Action:function(){var t=this,e="system/projectinfos/reset_params/",o={};c["a"].apiAjaxPost(e,o,(function(){l["a"].showToast(t.toastId),t.$emit("reset-started","reset-params")}),s["a"].defaultApiErrorHandler(e,""))}},watch:{},mounted:function(){}},v=S,I=Object(f["a"])(v,b,y,!1,null,null,null),h=I.exports,D=function(){var t=this,e=t._self._c;return e("div",[e("SimpleModalDlg",{attrs:{modalId:t.modalId,title:"恢复出厂设置",content:"",defaultButtonText:"取消",button2Text:"确认",button2Action:t.button2Action,dialogWidth:500},scopedSlots:t._u([{key:"bodyPost",fn:function(){return[e("IconFont",{staticStyle:{"font-size":"2em",color:"rgb(255, 186, 0)"},attrs:{iconName:"icon-tanhao"}}),t._v("\n    整个过程大约需要一到五分钟。授权信息、通道信息、检测参数和所有报警记录都将会删除。如需保存报警记录，请在“报警管理”中将数据下载到你的电脑。恢复出厂设置后，要再次使用需要重新激活。如忘记授权码，请联系厂家或销售人员。\n  ")]},proxy:!0}])}),e("Toast",{attrs:{toastId:t.toastId,text:"所有数据已删除，设备重启中"}})],1)},R=[],_=o("5f87"),C={name:"SystemFactoryResetConfirmDlg",components:{SimpleModalDlg:i["a"]},data:function(){return{toastId:s["a"].randomId("toast")}},props:{modalId:{type:String,required:!0}},computed:{},methods:{button2Action:function(){var t=this,e="system/projectinfos/factory_reset/",o={};c["a"].apiAjaxPost(e,o,(function(){l["a"].showToast(t.toastId),Object(_["g"])(),Object(_["b"])(),Object(_["a"])(),t.$emit("reset-started","factory-reset")}),s["a"].defaultApiErrorHandler(e,""))}},watch:{},mounted:function(){}},x=C,w=Object(f["a"])(x,D,R,!1,null,null,null),A=w.exports,j=function(){var t=this,e=t._self._c;return e("div",[e("SimpleModalDlg",{attrs:{modalId:t.modalId,title:"恢复出厂设置完成",content:"",defaultButtonText:"确认",defaultButtonAction:t.defaultButtonAction,dialogWidth:500},scopedSlots:t._u([{key:"bodyPost",fn:function(){return[e("IconFont",{staticStyle:{"font-size":"2em",color:"rgb(255, 186, 0)"},attrs:{iconName:"icon-tanhao"}}),t._v("\n    恢复出厂设置完成。请点击“确定”进入激活页面。\n  ")]},proxy:!0}])})],1)},F=[],T={name:"SystemFactoryResetSuccessDlg",components:{SimpleModalDlg:i["a"]},data:function(){return{}},props:{modalId:{type:String,required:!0}},computed:{},methods:{defaultButtonAction:function(){this.$router.push("/login")}},watch:{},mounted:function(){}},P=T,k=Object(f["a"])(P,j,F,!1,null,null,null),M=k.exports,O=o("1157"),z=o.n(O),B={name:"SysConfigRestartDevice",components:{SystemResetConfirmDlg:g,SystemFactoryResetConfirmDlg:A,SystemResetParamsConfirmDlg:h,SystemFactoryResetSuccessDlg:M},data:function(){return{deviceResetConfirmDlgId:s["a"].randomId("modal"),deviceResetParamsConfirmDlgId:s["a"].randomId("modal"),deviceFactoryResetConfirmDlgId:s["a"].randomId("modal"),deviceFactoryResetSuccessDlgId:s["a"].randomId("modal"),resetStarted:!1,apis:c["a"]}},computed:{},methods:{resetDone:function(t){t.resetStarted=!1},checkResetDone:function(t,e){var o=this;console.log("checkResetDone",t);var a="system/projectinfos/get_device_info/";t.apis.apiAjaxGet(a,{},(function(){t.resetDone(t),"factory-reset"===e&&z()("#".concat(o.deviceFactoryResetSuccessDlgId)).modal("show")}),(function(){setTimeout((function(){t.checkResetDone(t,e)}),5e3)}))},onResetStarted:function(t){var e=this;console.log("onResetStarted",this),this.resetStarted=!0;var o=this;setTimeout((function(){e.checkResetDone(o,t)}),3e4)}}},q=B,N=Object(f["a"])(q,a,n,!1,null,null,null);e["default"]=N.exports}}]);