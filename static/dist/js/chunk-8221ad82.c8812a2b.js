(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-8221ad82"],{"1ac9":function(t,e,a){"use strict";a("2d7b")},"1b04":function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[e("div",[e("div",{staticClass:"row"},[e("div",{staticClass:"col"},[e("ChannelAlgConfigPanel",{attrs:{algDisplayName:"算法检测默认参数",modalShown:!1,showTitle:!1,showRoi:!1,showTimeToggle:!1},model:{value:t.status,callback:function(e){t.status=e},expression:"status"}})],1)]),e("div",{staticClass:"row mt-2"},[e("div",{staticClass:"col modal-footer"},[e("button",{staticClass:"btn btn-primary btn-sm btn-iview-size",attrs:{type:"button"},on:{click:t.restoreStatus}},[t._v("恢复预设参数")]),e("button",{staticClass:"btn btn-primary btn-sm btn-iview-size",attrs:{type:"button"},on:{click:t.saveStatus}},[t._v("保存")])])])])]),e("Toast",{attrs:{toastId:t.toastId,text:"算法默认参数保存成功!"}})],1)},i=[],r=(a("8e6e"),a("ac6a"),a("456d"),a("ade3")),n=a("b84e"),o=a("fa7d"),l=a("0be2"),c=a("8715"),u=a("8cbb");function d(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(t);e&&(s=s.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,s)}return a}function m(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?d(Object(a),!0).forEach((function(e){Object(r["a"])(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):d(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}var f={name:"SysConfigDefaultAlgParams",components:{ChannelAlgConfigPanel:n["a"]},data:function(){return{toastId:o["a"].randomId("toast"),status:{currenRecordId:0,configured:!0}}},computed:{},methods:{loadStatus:function(){var t=this,e="algorithm/algorithmdefaultparameters/";l["a"].apiAjaxGet(e,{},(function(e){0===e.code&&(e.data.length>0?(t.currenRecordId=e.data[0].id,t.status=m({},e.data[0])):t.status=m({},c["a"].defaultAlgParams),t.status.configured=!0)}),o["a"].defaultApiErrorHandler(e,""))},saveStatus:function(){var t,e,a=this;this.currenRecordId?(t="algorithm/algorithmdefaultparameters/".concat(this.currenRecordId,"/"),e=l["a"].apiAjaxPut):(t="algorithm/algorithmdefaultparameters/",e=l["a"].apiAjaxPost);var s={analyze_interval:this.status.analyze_interval,alert_interval:this.status.alert_interval,alert_threshold:this.status.alert_threshold,alert_times:this.status.alert_times};e(t,s,(function(t){0===t.code&&(u["a"].showToast(a.toastId),a.loadStatus())}),o["a"].defaultApiErrorHandler(t,""))},restoreStatus:function(){var t=this;if(this.currenRecordId){var e="algorithm/algorithmdefaultparameters/".concat(this.currenRecordId,"/");l["a"].apiAjaxDelete(e,{},(function(){t.currenRecordId=0,t.loadStatus()}),o["a"].defaultApiErrorHandler(e,""))}}},watch:{status:{handler:function(t,e){console.log("status changed: ",t,e)},deep:!0}},mounted:function(){console.log("SysConfigDefaultAlgParams mounted"),this.loadStatus()}},p=f,v=a("2877"),g=Object(v["a"])(p,s,i,!1,null,null,null);e["default"]=g.exports},"2d7b":function(t,e,a){},b84e:function(t,e,a){"use strict";var s=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container-fluid"},[t.showTitle?e("div",{staticClass:"row w-100 ml-1 py-2 border-bottom"},[e("label",{staticClass:"mt-1 field-label"},[t._v("当前算法：")]),e("span",{staticClass:"mt-1 mr-4"},[t._v(t._s(t.algDisplayName)+"识别")]),e("label",{staticClass:"mt-1 field-label",attrs:{for:"id-channel-alg-config"}},[t._v("配置")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.status.configured,expression:"status.configured"}],staticClass:"ml-1",attrs:{type:"radio",id:"id-channel-alg-config",name:"channelAlgConfig"},domProps:{value:!0,checked:t._q(t.status.configured,!0)},on:{change:function(e){return t.$set(t.status,"configured",!0)}}}),e("label",{staticClass:"ml-2 mt-1 field-label",attrs:{for:"id-channel-alg-unconfig"}},[t._v("不配置")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.status.configured,expression:"status.configured"}],staticClass:"ml-2",attrs:{type:"radio",id:"id-channel-alg-unconfig",name:"channelAlgConfig"},domProps:{value:!1,checked:t._q(t.status.configured,!1)},on:{change:function(e){return t.$set(t.status,"configured",!1)}}}),e("button",{staticClass:"btn btn-sm btn-primary ml-2 btn-sm btn-iview-size",attrs:{type:"button"},on:{click:t.restoreDefault}},[t._v("恢复默认参数")])]):t._e(),e("div",{directives:[{name:"show",rawName:"v-show",value:t.status.configured,expression:"status.configured"}],staticClass:"row mt-2 pb-2 border-bottom"},[e("span",{staticClass:"field-label pl-3"},[t._v("检测参数：")]),e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[t._m(0),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model.number",value:t.status.analyze_interval,expression:"status.analyze_interval",modifiers:{number:!0}}],staticClass:"ml-2",attrs:{type:"number",step:"500"},domProps:{value:t.status.analyze_interval},on:{input:function(e){e.target.composing||t.$set(t.status,"analyze_interval",t._n(e.target.value))},blur:function(e){return t.$forceUpdate()}}}),e("span",{},[t._v("(500毫秒为单位，最小值1000毫秒)")])])]),e("div",{staticClass:"row mt-1"},[t._m(1),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model.number",value:t.status.alert_interval,expression:"status.alert_interval",modifiers:{number:!0}}],staticClass:"ml-2",attrs:{type:"number",step:"1"},domProps:{value:t.status.alert_interval},on:{input:function(e){e.target.composing||t.$set(t.status,"alert_interval",t._n(e.target.value))},blur:function(e){return t.$forceUpdate()}}})])]),e("div",{staticClass:"row mt-1"},[t._m(2),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model.number",value:t.status.alert_threshold,expression:"status.alert_threshold",modifiers:{number:!0}}],staticClass:"ml-2",attrs:{type:"number",step:"0.05"},domProps:{value:t.status.alert_threshold},on:{input:function(e){e.target.composing||t.$set(t.status,"alert_threshold",t._n(e.target.value))},blur:function(e){return t.$forceUpdate()}}}),e("span",{},[t._v("(值越大检查准确率越高)")])])])])]),e("div",{directives:[{name:"show",rawName:"v-show",value:t.status.configured,expression:"status.configured"}],staticClass:"row mt-2 pb-2 border-bottom"},[e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row mb-1"},[e("span",{staticClass:"field-label pl-3 pt-1"},[t._v("布控时间：")]),e("a",{directives:[{name:"show",rawName:"v-show",value:t.showTimeToggle,expression:"showTimeToggle"}],staticClass:"btn-sm btn-primary",attrs:{"data-toggle":"collapse",href:"#dateTimeSetting",role:"button","aria-expanded":"false","aria-controls":"dateTimeSetting"}},[t._v(t._s(t.dateTimeSettingShown?"收起":"展开"))])]),e("div",{staticClass:"row"},[e("div",{class:"col collapse ".concat(t.showTimeToggle?"":"show"),attrs:{id:"dateTimeSetting"}},[e("div",{staticClass:"border w-100",staticStyle:{height:"400px"}},[e("WeekDatetimePicker",{model:{value:t.status.alert_times,callback:function(e){t.$set(t.status,"alert_times",e)},expression:"status.alert_times"}})],1)])])])]),e("div",{directives:[{name:"show",rawName:"v-show",value:t.status.configured&&t.showRoi,expression:"status.configured && showRoi"}],staticClass:"row mt-2 border-bottom"},[e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[e("span",{staticClass:"field-label py-2 pl-3"},[t._v("绘制监控区域(ROI)：")]),e("a",{staticClass:"mr-2",attrs:{title:t.roiDrawing?"完成":"新建多边形",href:"javascript:void(0);"},on:{click:function(e){t.roiDrawing=!t.roiDrawing}}},[e("IconFont",{class:t.roiDrawing?"duobianxing-selected":"duobianxing-unselected",attrs:{iconName:"icon-duobianxingxuanze"}})],1),e("a",{staticClass:"mr-2",attrs:{title:"清除选区(监控整个画面)",href:"javascript:void(0);"},on:{click:function(e){t.status.roi_region=null,t.roiDrawing=!1}}},[e("IconFont",{staticClass:"shanchu-button",attrs:{iconName:"icon-shanchu"}})],1)]),e("div",{staticClass:"row mt-2"},[e("div",{staticClass:"col"},[e("RoiDrawPanel",{attrs:{isDrawing:t.roiDrawing,imgSrc:t.channelImage,panelShown:t.modalShown&&t.status.configured},model:{value:t.status.roi_region,callback:function(e){t.$set(t.status,"roi_region",e)},expression:"status.roi_region"}})],1)])])])])},i=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"col-3 text-right"},[e("span",{},[t._v("分析间隔(毫秒)")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"col-3 text-right"},[e("span",{},[t._v("报警间隔(秒)")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"col-3 text-right"},[e("span",{},[t._v("报警阈值(0-1)")])])}],r=(a("8e6e"),a("ac6a"),a("456d"),a("ade3")),n=a("f62b"),o=a("4865"),l=a("d940");function c(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(t);e&&(s=s.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,s)}return a}function u(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?c(Object(a),!0).forEach((function(e){Object(r["a"])(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):c(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}var d={name:"ChannelAlgConfigPanel",components:{WeekDatetimePicker:n["a"],RoiDrawPanel:o["a"],IconFont:l["a"]},data:function(){return{dateTimeSettingShown:!1,status:{},algDisplayNamePrev:"",roiDrawing:!1}},props:{defaultParameters:{type:Object,required:!1,default:function(){return{}}},showTimeToggle:{type:Boolean,required:!1,default:!0},showTitle:{type:Boolean,required:!1,default:!0},showRoi:{type:Boolean,required:!1,default:!0},channelImage:{type:String,required:!1,default:""},modalShown:{type:Boolean,required:!1,default:!1},algDisplayName:{type:String,required:!0},modelValue:{type:Object,required:!0}},model:{prop:"modelValue",event:"input"},computed:{},methods:{restoreDefault:function(){var t=u({},this.status);for(var e in this.defaultParameters)t[e]=this.defaultParameters[e];this.status=t}},watch:{modelValue:function(t){this.algDisplayNamePrev===this.algDisplayName&&JSON.stringify(this.status)===JSON.stringify(t)||(this.algDisplayNamePrev=this.algDisplayName,this.status=this.modelValue)},status:{handler:function(){console.log("this.status changed",this.status),this.$emit("input",this.status)},deep:!0},algDisplayName:function(){this.roiDrawing=!1}},mounted:function(){this.status=u({},this.modelValue)}},m=d,f=(a("1ac9"),a("2877")),p=Object(f["a"])(m,s,i,!1,null,null,null);e["a"]=p.exports}}]);