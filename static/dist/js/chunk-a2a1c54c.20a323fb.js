(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-a2a1c54c"],{"15b7":function(t,e,a){},"33de":function(t,e,a){"use strict";a("cfd2")},"36bd":function(t,e,a){"use strict";var n=a("4bf8"),i=a("77f1"),s=a("9def");t.exports=function(t){var e=n(this),a=s(e.length),l=arguments.length,r=i(l>1?arguments[1]:void 0,a),o=l>2?arguments[2]:void 0,c=void 0===o?a:i(o,a);while(c>r)e[r++]=t;return e}},"3dba":function(t,e,a){"use strict";a("7bed")},"405b":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row ml-2 mb-2"},[e("div",{staticClass:"w-100",staticStyle:{display:"flex","justify-content":"space-between"}},[e("SimpleSelect",{attrs:{itemList:t.algNameChs},model:{value:t.currAlgIndex,callback:function(e){t.currAlgIndex=e},expression:"currAlgIndex"}}),e("button",{staticClass:"btn btn-primary mr-4 btn-sm btn-iview-size",on:{click:t.saveCurrent}},[t._v("保存")])],1)]),e("div",{staticClass:"row"},[e("div",{staticClass:"col-xl-2 algorithm-config-block"},[e("div",{staticClass:"card w-100"},[t._m(0),e("div",{staticClass:"card-body py-1 px-2 col algorithm-config-block-body alg-left-panel-flat"},[e("div",{staticClass:"ml-2"},[e("label",{staticClass:"mt-1 field-label",attrs:{for:"id-channel-alg-config"}},[t._v("开启")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.algStatus[t.selectedCno-1].configured,expression:"algStatus[selectedCno-1].configured"}],staticClass:"ml-1",attrs:{type:"radio",id:"id-channel-alg-config",name:"channelAlgConfig"},domProps:{value:!0,checked:t._q(t.algStatus[t.selectedCno-1].configured,!0)},on:{change:function(e){return t.$set(t.algStatus[t.selectedCno-1],"configured",!0)}}}),e("label",{staticClass:"ml-2 mt-1 field-label",attrs:{for:"id-channel-alg-unconfig"}},[t._v("不开启")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.algStatus[t.selectedCno-1].configured,expression:"algStatus[selectedCno-1].configured"}],staticClass:"ml-2",attrs:{type:"radio",id:"id-channel-alg-unconfig",name:"channelAlgConfig"},domProps:{value:!1,checked:t._q(t.algStatus[t.selectedCno-1].configured,!1)},on:{change:function(e){return t.$set(t.algStatus[t.selectedCno-1],"configured",!1)}}})]),e("ChannelSelectionGrid",{attrs:{channelNames:t.channelNames,channelConfigured:t.channelConfigured,channelStatusChanged:t.channelStatusChanged},model:{value:t.selectedCno,callback:function(e){t.selectedCno=e},expression:"selectedCno"}})],1)])]),e("div",{staticClass:"col-xl-10 pl-0"},[e("div",{staticClass:"w-100 overflow-auto container-fluid"},[e("ChannelAlgConfigPanelFlat",{attrs:{algDisplayName:"来自于算法配置",channelImage:t.channelImage,modalShown:t.modalShown,defaultParameters:t.defaultParameters,roiDiscardDrawing:t.roiDiscardDrawing},model:{value:t.algStatus[t.selectedCno-1],callback:function(e){t.$set(t.algStatus,t.selectedCno-1,e)},expression:"algStatus[selectedCno-1]"}})],1)])]),e("Toast",{attrs:{toastId:t.toastId,text:"算法配置保存成功！"}})],1)},i=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"card-header py-1 px-2 dash-chart-title"},[e("span",{staticClass:"card-head-title"},[t._v("请选择通道")])])}],s=(a("8e6e"),a("2909")),l=(a("7f7f"),a("ade3")),r=(a("6c7b"),a("ac6a"),a("456d"),a("fa7d")),o=a("f953"),c=a("0be2"),u=a("8715"),d=a("1157"),h=a.n(d),m=function(){var t=this,e=t._self._c;return e("div",{staticClass:"row"},[e("div",{staticClass:"col-lg-7 ml-0 pl-0 algorithm-config-block"},[e("div",{staticClass:"card w-100"},[t._m(0),e("div",{staticClass:"card-body py-1 px-2 col algorithm-config-block-body alg-mid-panel-flat"},[e("div",{directives:[{name:"show",rawName:"v-show",value:t.status.configured&&t.showRoi,expression:"status.configured && showRoi"}],staticClass:"row mt-2"},[e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[e("div",{staticClass:"col"},[e("div",{staticClass:"row mx-0"},[e("a",{staticClass:"mr-2 icon-anchor",attrs:{title:t.roiDrawing?"完成":"新建多边形监控区域",href:"javascript:void(0);"},on:{click:function(e){t.roiDrawing=!t.roiDrawing}}},[e("IconFont",{class:t.roiDrawing?"duobianxing-selected":"duobianxing-unselected",attrs:{iconName:"icon-duobianxingxuanze"}})],1),e("a",{staticClass:"mr-2 icon-anchor",attrs:{title:"清除所有选区(全域监控)",href:"javascript:void(0);"},on:{click:function(e){t.roiClearFlag=!t.roiClearFlag,t.roiDrawing=!1}}},[e("IconFont",{staticClass:"shanchu-button",attrs:{iconName:"icon-shanchu"}})],1)])])]),e("div",{staticClass:"row mx-0 mt-2"},[e("div",{staticClass:"col px-0"},[e("RoiDrawPanel",{attrs:{isDrawing:t.roiDrawing,imgSrc:t.channelImage,panelShown:t.modalShown&&t.status.configured,clearFlag:t.roiClearFlag,discardDrawing:t.discardDrawing},on:{"drawing-discarded":function(e){t.roiDrawing=!1}},model:{value:t.status.roi_region,callback:function(e){t.$set(t.status,"roi_region",e)},expression:"status.roi_region"}})],1)])])])])])]),e("div",{staticClass:"col-xl-5 ml-0 pl-0 algorithm-config-block"},[e("div",{staticClass:"card w-100"},[t._m(1),e("div",{staticClass:"card-body py-1 px-2 col algorithm-config-block-body alg-right-panel-flat"},[e("div",{directives:[{name:"show",rawName:"v-show",value:t.status.configured,expression:"status.configured"}],staticClass:"row mt-2 pb-2"},[e("span",{staticClass:"field-label pl-3"},[t._v("基本参数：")]),e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[t._m(2),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model.number",value:t.status.analyze_interval,expression:"status.analyze_interval",modifiers:{number:!0}}],staticClass:"ml-2",attrs:{type:"number",step:"500"},domProps:{value:t.status.analyze_interval},on:{input:function(e){e.target.composing||t.$set(t.status,"analyze_interval",t._n(e.target.value))},blur:function(e){return t.$forceUpdate()}}}),e("span",{})])]),e("div",{staticClass:"row mt-1"},[t._m(3),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model.number",value:t.status.alert_interval,expression:"status.alert_interval",modifiers:{number:!0}}],staticClass:"ml-2",attrs:{type:"number",step:"1"},domProps:{value:t.status.alert_interval},on:{input:function(e){e.target.composing||t.$set(t.status,"alert_interval",t._n(e.target.value))},blur:function(e){return t.$forceUpdate()}}})])]),e("div",{staticClass:"row mt-1"},[t._m(4),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model.number",value:t.status.alert_threshold,expression:"status.alert_threshold",modifiers:{number:!0}}],staticClass:"ml-2",attrs:{type:"number",step:"0.05"},domProps:{value:t.status.alert_threshold},on:{input:function(e){e.target.composing||t.$set(t.status,"alert_threshold",t._n(e.target.value))},blur:function(e){return t.$forceUpdate()}}}),e("span",{})])])])]),e("div",{directives:[{name:"show",rawName:"v-show",value:t.status.configured,expression:"status.configured"}],staticClass:"row mt-2 pb-2"},[e("div",{staticClass:"container-fluid"},[t._m(5),e("div",{staticClass:"row"},[e("div",{staticClass:"col collapse show",attrs:{id:"dateTimeSetting"}},[e("div",{staticClass:"w-100",staticStyle:{height:"400px"}},[e("WeekDatetimePicker",{model:{value:t.status.alert_times,callback:function(e){t.$set(t.status,"alert_times",e)},expression:"status.alert_times"}})],1)])])])])])])])])},f=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"card-header py-1 px-2 dash-chart-title"},[e("span",{staticClass:"card-head-title"},[t._v("请绘制ROI（监控区域）")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"card-header py-1 px-2 dash-chart-title"},[e("span",{staticClass:"card-head-title"},[t._v("请配置监控参数")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"col-4 text-right"},[e("span",{staticClass:"field-required"},[t._v("分析间隔(毫秒)")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"col-4 text-right"},[e("span",{staticClass:"field-required"},[t._v("报警间隔(秒)")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"col-4 text-right"},[e("span",{staticClass:"field-required"},[t._v("报警阈值(0-1)")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"row mb-1"},[e("span",{staticClass:"field-label pl-3 pt-1"},[t._v("布控时间：")])])}],g=function(){var t=this,e=t._self._c;return e("div",{staticClass:"w-100 h-100 overflow-hidden"},[e("div",{staticClass:"row",staticStyle:{height:"10px"}}),e("div",{staticClass:"row mx-0"},[e("div",[e("label",{staticClass:"ml-2 mr-2 pl-2",attrs:{for:t.uniqueId+"weekday-same"}},[t._v("每天监控时段相同")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.weekdaySame,expression:"weekdaySame"}],attrs:{type:"checkbox",id:t.uniqueId+"weekday-same"},domProps:{checked:Array.isArray(t.weekdaySame)?t._i(t.weekdaySame,null)>-1:t.weekdaySame},on:{change:function(e){var a=t.weekdaySame,n=e.target,i=!!n.checked;if(Array.isArray(a)){var s=null,l=t._i(a,s);n.checked?l<0&&(t.weekdaySame=a.concat([s])):l>-1&&(t.weekdaySame=a.slice(0,l).concat(a.slice(l+1)))}else t.weekdaySame=i}}})])]),t._l(t.weekdays,(function(a,n){return e("div",{key:t.uniqueId+"-weekday-"+n,staticClass:"row mx-0 my-0"},[e("div",{staticClass:"pl-2 py-2 text-center",staticStyle:{width:"16%"}},[e("label",{staticClass:"mr-2",attrs:{for:t.uniqueId+"weekday-selected"+n}},[t._v("星期"+t._s(a))]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.dayStatus[n],expression:"dayStatus[i]"}],attrs:{type:"checkbox",id:t.uniqueId+"weekday-selected"+n},domProps:{checked:Array.isArray(t.dayStatus[n])?t._i(t.dayStatus[n],null)>-1:t.dayStatus[n]},on:{change:function(e){var a=t.dayStatus[n],i=e.target,s=!!i.checked;if(Array.isArray(a)){var l=null,r=t._i(a,l);i.checked?r<0&&t.$set(t.dayStatus,n,a.concat([l])):r>-1&&t.$set(t.dayStatus,n,a.slice(0,r).concat(a.slice(r+1)))}else t.$set(t.dayStatus,n,s)}}})]),e("div",{},[e("div",{staticClass:"d-flex"},t._l(new Array(25).fill(0).map((function(t,e){return e})),(function(a,i){return e("div",{key:t.uniqueId+"-time-label-"+n+"-"+i,staticClass:"time-label-sm"},[t._v("\n          "+t._s(a)+"\n        ")])})),0),e("div",{staticClass:"time-tick-sm ml-1 mr-0"}),e("div",{staticClass:"time-bar-container"},[e("div",{staticClass:"time-bar-sm ml-1 mr-0"},t._l(new Array(t.dayCellNum).fill(0).map((function(t,e){return e})),(function(a,i){return e("div",{key:t.uniqueId+"-time-cell-"+n+"-"+i,class:"time-cell-sm"+(t.cellStatus[n*t.dayCellNum+i]?" cell-selected":"")+(t.dayStatus[n]?"":" day-disabled")})})),0),e("div",{staticClass:"time-bar-sm-overlay ml-1 mr-0",on:{mousedown:function(e){return e.stopPropagation(),t.onTimeBarDown(e,n)},mousemove:function(e){return e.stopPropagation(),t.onTimeBarMove(e,n)},mouseout:function(e){return e.stopPropagation(),t.onTimeBarOut(e,n)},mouseup:function(e){return e.stopPropagation(),t.onTimeBarUp(e,n)}}})])]),e("div",{staticClass:"pl-2 py-2 text-center",staticStyle:{width:"4%"}},[e("a",{staticClass:"popover-dismiss",attrs:{type:"button",role:"button","data-toggle":"popover",title:"","data-content":t.getDayTimeDesc(n),"data-original-title":"已设置时间段"}},[e("IconFont",{attrs:{iconName:"icon-xiangxixinxi"}})],1)])])}))],2)},p=[],v=8,w=7,y=30,C=1440/y,S=w*C;function b(){for(var t=new Array(S).fill(0),e=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,40,41,42,43,44,45,46,47],a=function(a){e.forEach((function(e){t[a*C+e]=1}))},n=0;n<w;n++)a(n);return t}var _={name:"WeekDatetimePicker",components:{},data:function(){return{uniqueId:r["a"].randomId("uniqueId"),currDay:-1,weekdayNum:w,dayCellNum:C,timeCellSize:y,dayStatus:new Array(w).fill(!0),cellStatus:b(),weekdaySame:!1,weekdays:["一","二","三","四","五","六","日"],cellStart:-1,cellEnd:-1,cellBackup:null}},props:{modelValue:{type:String}},model:{prop:"modelValue",event:"input"},computed:{},methods:{formatTimeValue:function(t){return t<10?"0".concat(t):"".concat(t)},getDayTimeSegs:function(t){var e=[],a=0;while(a<this.dayCellNum){while(a<this.dayCellNum&&!this.cellStatus[t*this.dayCellNum+a])a+=1;if(a<this.dayCellNum){var n=a;while(a<this.dayCellNum&&this.cellStatus[t*this.dayCellNum+a])a+=1;var i=a;e.push([n*this.timeCellSize,i*this.timeCellSize])}}return e},segsToCellStatus:function(t){var e=this,a=new Array(S).fill(0);t.forEach((function(t,n){t.segs.forEach((function(t){for(var i=Math.floor(t[0]/y),s=Math.ceil(t[1]/y),l=i;l<s;l++)a[n*e.dayCellNum+l]=1}))})),this.cellStatus=a},getDayTimeDesc:function(t){var e=this,a="",n=this.getDayTimeSegs(t);return a=n.map((function(t){return"".concat(e.formatTimeValue(Math.floor(t[0]/60)),":").concat(e.formatTimeValue(t[0]%60),"-").concat(e.formatTimeValue(Math.floor(t[1]/60)),":").concat(e.formatTimeValue(t[1]%60))})).join(";"),a},getDateTimeSettings:function(){for(var t=[],e=0;e<this.weekdayNum;e++)t.push({enabled:this.dayStatus[e],segs:this.getDayTimeSegs(e)});return t},setDateTimeSettings:function(t){var e=this;t&&t.length===this.weekdayNum&&(t.forEach((function(t,a){e.dayStatus[a]^t.enabled&&(e.dayStatus[a]=t.enabled)})),this.segsToCellStatus(t))},makeWeekdaySame:function(t){for(var e=0;e<this.weekdayNum;e++)if(e!==t)for(var a=0;a<this.dayCellNum;a++)this.cellStatus[e*this.dayCellNum+a]=this.cellStatus[t*this.dayCellNum+a]},barOffset2CellIndex:function(t){return parseInt(t/v)},onTimeBarDown:function(t,e){if(1===t.buttons&&this.dayStatus[e]){this.currDay=e;var a=this.barOffset2CellIndex(t.offsetX);this.cellStart=a,this.cellEnd=a,this.cellBackup=this.cellStatus.slice(e*this.dayCellNum,(e+1)*this.dayCellNum),this.cellStatus[e*this.dayCellNum+a]^=1,this.cellStatus=Object(s["a"])(this.cellStatus),this.weekdaySame&&this.makeWeekdaySame(this.currDay)}},onTimeBarMove:function(t,e){var a;if(1===t.buttons&&!(this.currDay<0||e!==this.currDay)){var n=this.barOffset2CellIndex(t.offsetX);if(n!==this.cellEnd){this.cellEnd=n;var i=this.cellStatus[e*this.dayCellNum+this.cellStart];(a=this.cellStatus).splice.apply(a,[e*this.dayCellNum,this.dayCellNum].concat(Object(s["a"])(this.cellBackup)));for(var l=Math.min(this.cellStart,this.cellEnd);l<=Math.max(this.cellStart,this.cellEnd);l++)this.cellStatus[e*this.dayCellNum+l]=i;this.cellStatus=Object(s["a"])(this.cellStatus),this.weekdaySame&&this.makeWeekdaySame(this.currDay)}}},onTimeBarOut:function(t,e){1===t.buttons&&(this.currDay<0||this.currDay)},onTimeBarUp:function(t,e){1===t.buttons&&(this.currDay=-1)}},watch:{weekdaySame:function(){this.weekdaySame&&this.makeWeekdaySame(0),this.$emit("input",JSON.stringify(this.getDateTimeSettings()))},dayStatus:{handler:function(){this.$emit("input",JSON.stringify(this.getDateTimeSettings()))},deep:!0},cellStatus:function(){this.$emit("input",JSON.stringify(this.getDateTimeSettings()))},modelValue:function(t){t?this.setDateTimeSettings(JSON.parse(t)):(this.dayStatus=new Array(w).fill(!0),this.cellStatus=b())}},mounted:function(){h()((function(){h()('[data-toggle="popover"]').popover()}))}},x=_,D=(a("c073"),a("2877")),I=Object(D["a"])(x,g,p,!1,null,null,null),k=I.exports,P=function(){var t=this,e=t._self._c;return e("div",{staticClass:"w-100 roi-preview-image",attrs:{id:"roiImageBox"}},[e("div",{directives:[{name:"show",rawName:"v-show",value:!t.imgSrc,expression:"!imgSrc"}],staticClass:"waitingImage justify-content-center"},[e("div",{staticClass:"waitPrompt"},[e("Icon",{attrs:{type:"md-videocam"}}),e("span",[t._v("摄像头画面加载中......")])],1)]),e("img",{directives:[{name:"show",rawName:"v-show",value:t.imgSrc,expression:"imgSrc"}],class:t.roiImgClass,attrs:{id:"roiImageId",src:t.imgSrc,alt:"摄像头画面加载中......"}}),e("canvas",{class:t.roiCanvasClass,attrs:{id:t.canvasId,width:t.canvasWidth,height:t.canvasHeight},on:{mousedown:function(e){return t.onMouseDown(e)},mousemove:function(e){return t.onMouseMove(e)},mouseup:function(e){return t.onMouseUp()},click:function(e){return t.onClick(e)},dblclick:function(e){return t.onDoubleClick(e)}}})])},N=[],O={name:"RoiDrawPanel",components:{},data:function(){return{canvasId:r["a"].randomString(),roiImageId:r["a"].randomString(),roiImgClass:"roiImgClassNormal",roiCanvasClass:"roiCanvasClassNormal",canvasWidth:1,canvasHeight:1,roiPaths:[],drawingPath:[],mouseIsDown:!1,mouseCurrX:0,mouseCurrY:0}},props:{imgSrc:{type:String,required:!1,default:""},panelShown:{type:Boolean,required:!1,default:!1},isDrawing:{type:Boolean,required:!1,default:!1},clearFlag:{type:Boolean,required:!0},discardDrawing:{type:Boolean,required:!0},modelValue:{required:!0}},model:{prop:"modelValue",event:"input"},computed:{},methods:{canvasBoxToImageBox:function(){},imageBoxToCanvasBox:function(){},imageLoaded:function(){var t=this,e=document.getElementById(this.roiImageId);this.panelShown&&e&&e.naturalWidth?(this.canvasWidth=e.width,this.canvasHeight=e.height,this.loadRoiPaths(this.modelValue),setTimeout((function(){t.drawRois()}),200)):setTimeout((function(){return t.imageLoaded()}),300)},drawPath:function(t,e,a){0!==e.length&&(t.save(),a?(t.strokeStyle="rgba(30, 200, 30, 1)",t.fillStyle="rgba(30, 200, 30, 1)",t.fillRect(e[0][0]-1,e[0][1]-1,3,3)):t.strokeStyle="rgba(30, 30, 200, 1)",t.beginPath(),t.lineWidth=2,t.moveTo(e[0][0],e[0][1]),e.slice(1).forEach((function(e){return t.lineTo(e[0],e[1])})),t.closePath(),t.stroke(),t.restore())},drawRois:function(){var t=this,e=document.getElementById(this.canvasId),a=document.createElement("canvas");if(a.width=e.width,a.height=e.height,0!==a.width&&0!==a.height){var n,i=a.getContext("2d");this.roiPaths.forEach((function(e){t.drawPath(i,e,!1)})),n=this.mouseIsDown?[].concat(Object(s["a"])(this.drawingPath),[[this.mouseCurrX,this.mouseCurrY]]):this.drawingPath,n.length&&this.drawPath(i,n,!0);var l=i.getImageData(0,0,a.width,a.height),r=e.getContext("2d");r.putImageData(l,0,0)}},filterRoiPaths:function(){},roiPathsToEvent:function(){if(!this.roiPaths.length)return null;var t=document.getElementById(this.roiImageId),e=t.naturalWidth/this.canvasWidth,a=t.naturalHeight/this.canvasHeight,n=this.roiPaths.map((function(t){return t.map((function(t){return[Math.round(t[0]*e),Math.round(t[1]*a)]}))}));return console.log("roiPathsToEvent",n),JSON.stringify(n)},resetRois:function(){this.roiPaths=[],this.drawingPath=[]},loadRoiPaths:function(t){if(t){var e=document.getElementById(this.roiImageId);try{var a=this.canvasWidth/e.naturalWidth,n=this.canvasHeight/e.naturalHeight,i=JSON.parse(t);this.roiPaths=i.map((function(t){return t.map((function(t){return[Math.round(t[0]*a),Math.round(t[1]*n)]}))}))}catch(s){console.log("loadRoiPaths exception",s)}console.log("loadRoiPaths",this.roiPaths)}else this.resetRois()},onMouseDown:function(t){console.log("onMouseDown",t),this.isDrawing&&1===t.buttons&&(this.mouseIsDown=!0,this.mouseCurrX=t.offsetX,this.mouseCurrY=t.offsetY,this.drawRois())},onMouseMove:function(t){this.isDrawing&&1===t.buttons&&this.mouseIsDown&&this.drawingPath.length&&(this.mouseCurrX=t.offsetX,this.mouseCurrY=t.offsetY,this.drawRois())},onMouseUp:function(t){console.log("onMouseUp",t),this.isDrawing&&this.mouseIsDown&&(this.mouseIsDown=!1,this.drawingPath.push([this.mouseCurrX,this.mouseCurrY]))},onClick:function(t){console.log("onClick",t)},onDoubleClick:function(t){console.log("onDoubleClick",t)}},watch:{isDrawing:function(){!this.isDrawing&&this.drawingPath.length>=3&&(this.roiPaths.push(this.drawingPath),this.$emit("input",this.roiPathsToEvent())),this.drawingPath=[],this.drawRois()},clearFlag:function(){this.resetRois(),this.$emit("input",this.roiPathsToEvent())},discardDrawing:function(){this.drawingPath=[],this.drawRois(),this.$emit("drawing-discarded")},panelShown:function(){var t=this;this.panelShown&&setTimeout((function(){return t.imageLoaded()}),500)},modelValue:function(){console.log("roi modelValue changed",this.modelValue),this.drawingPath=[],this.loadRoiPaths(this.modelValue),this.drawRois()}},mounted:function(){}},A=O,j=(a("33de"),Object(D["a"])(A,P,N,!1,null,null,null)),T=j.exports,q=a("d940");function B(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function E(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?B(Object(a),!0).forEach((function(e){Object(l["a"])(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):B(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}var $={name:"ChannelAlgConfigPanelFlat",components:{WeekDatetimePicker:k,RoiDrawPanel:T,IconFont:q["a"]},data:function(){return{dateTimeSettingShown:!1,status:{},algDisplayNamePrev:"",roiDrawing:!1,roiClearFlag:!1,discardDrawing:!1}},props:{defaultParameters:{type:Object,required:!1,default:function(){return{}}},showTimeToggle:{type:Boolean,required:!1,default:!0},showTitle:{type:Boolean,required:!1,default:!0},showRoi:{type:Boolean,required:!1,default:!0},roiDiscardDrawing:{type:Boolean,required:!0},channelImage:{type:String,required:!1,default:""},modalShown:{type:Boolean,required:!1,default:!1},algDisplayName:{type:String,required:!0},modelValue:{type:Object,required:!0}},model:{prop:"modelValue",event:"input"},computed:{},methods:{restoreDefault:function(){var t=E({},this.status);for(var e in this.defaultParameters)t[e]=this.defaultParameters[e];this.status=t}},watch:{modelValue:function(t){console.log("modelValue changed",t),this.algDisplayNamePrev=this.algDisplayName,this.status=t,this.discardDrawing=!this.discardDrawing},roiDiscardDrawing:function(){this.discardDrawing=this.roiDiscardDrawing},status:{handler:function(){parseInt(this.status.analyze_interval)<1e3&&(this.status.analyze_interval="1000"),parseInt(this.status.alert_interval)<30&&(this.status.alert_interval="30"),parseFloat(this.status.alert_threshold)<0&&(this.status.alert_threshold="0"),parseFloat(this.status.alert_threshold)>1&&(this.status.alert_threshold="1"),this.$emit("input",this.status)},deep:!0},algDisplayName:function(){this.roiDrawing=!1}},mounted:function(){this.status=E({},this.modelValue)}},V=$,R=(a("c8da"),Object(D["a"])(V,m,f,!1,null,null,null)),M=R.exports,F=function(){var t=this,e=t._self._c;return e("div",{staticClass:"alg-channel-list",attrs:{id:"list-tab",role:"tablist"}},t._l(new Array(t.maxChannels).fill(0).map((function(t,e){return e+1})),(function(n){return e("div",{key:n,staticClass:"text-center alg-channel-item",on:{click:function(e){return t.channelClicked(n)}}},[e("img",{directives:[{name:"show",rawName:"v-show",value:t.channelConfigured[n-1],expression:"channelConfigured[item-1]"}],class:"alg-channel-icon "+(n===t.selectedCno?"alg-channel-icon-selected ":" ")+(t.channelNames[n-1]?" ":"alg-channel-icon-invalid "),attrs:{src:a("5289"),alt:"通道"+{item:n}}}),e("img",{directives:[{name:"show",rawName:"v-show",value:!t.channelConfigured[n-1],expression:"!channelConfigured[item-1]"}],class:"alg-channel-icon "+(n===t.selectedCno?"alg-channel-icon-selected ":" ")+(t.channelNames[n-1]?" ":"alg-channel-icon-invalid "),attrs:{src:a("cc1e"),alt:"通道"+{item:n}}}),e("div",{staticClass:"text-center"},[e("IconFont",{class:t.channelNames[n-1]?t.channelStatusChanged[n-1]?"red-dot":"green-dot":"gray-dot",attrs:{iconName:"icon-dot"}}),t._v("\n      "+t._s("".concat(n," ")+(t.channelNames[n-1]?t.channelNames[n-1]:"(未添加)"))+"\n    ")],1)])})),0)},W=[],z=(a("c5f6"),a("f121")),H={name:"ChannelSelectionGrid",components:{},data:function(){return{maxChannels:z["a"].maxChannels}},props:{channelConfigured:{type:Array,required:!0},channelStatusChanged:{type:Array,required:!0},channelNames:{type:Array,required:!0},selectedCno:{type:Number,required:!0}},model:{prop:"selectedCno",event:"input"},methods:{channelClicked:function(t){this.channelNames[t-1]&&t!==this.selectedCno&&this.$emit("input",t)}},watch:{selectedCno:function(){}},mounted:function(){}},U=H,J=(a("87ae"),Object(D["a"])(U,F,W,!1,null,null,null)),X=J.exports,G=a("4d92"),Y=a("8cbb");function L(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function K(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?L(Object(a),!0).forEach((function(e){Object(l["a"])(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):L(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}var Q={name:"AlgorithmAlgConfigPage",components:{SimpleModalDlg:o["a"],ChannelAlgConfigPanelFlat:M,ChannelSelectionGrid:X,SimpleSelect:G["a"]},data:function(){return{toastId:r["a"].randomId("toast"),algorithmInfo:u["a"].getAlgNameIcons(),algNames:Object.keys(u["a"].getAlgNameIcons()),algNameChs:Object.keys(u["a"].getAlgNameIcons()).map((function(t){return u["a"].getAlgNameIcons()[t].name_ch+"识别"})),algStatus:new Array(z["a"].maxChannels).fill(0).map((function(){return K({configured:!1},u["a"].defaultAlgParams)})),dateTimeSettingShown:!1,channelImage:"",modalShown:!1,defaultParameters:{},selectedCno:1,channelConfigured:new Array(z["a"].maxChannels).fill(!1),channelIds:new Array(z["a"].maxChannels).fill(0),channelNames:new Array(z["a"].maxChannels).fill(""),channelStatusOld:new Array(z["a"].maxChannels).fill(""),channelStatusChanged:new Array(z["a"].maxChannels).fill(!1),currAlg:{},currAlgIndex:0,updated:!1,roiDiscardDrawing:!1}},props:{},computed:{},methods:{saveCurrent:function(){var t=this,e=this.selectedCno,a=this.channelIds[this.selectedCno-1],n="channel/channels/".concat(a,"/config_single_alg/"),i={alg_name:this.currAlg.name,status:this.algStatus[e-1]};c["a"].apiAjaxPost(n,i,(function(n){0===n.code?(Y["a"].showToast(t.toastId),t.$emit("alg-channel-single-saved")):alert("算法配置保存失败(".concat(n.code,"): ").concat(n.message)),t.loadAlgorithmChannels(a,e)}),r["a"].defaultApiErrorHandler(n,"")),this.roiDiscardDrawing=!this.roiDiscardDrawing},recordToStatus:function(t){var e={};return Object.keys(this.defaultParameters).forEach((function(a){e[a]=t[a]})),e.configured=!0,e},loadChannelImage:function(){var t=this;console.log("loadChannelImage",this.selectedCno,this.channelIds);var e=this.channelIds[this.selectedCno-1];if(e){var a="channel/channels/".concat(e,"/get_real_time_image/");c["a"].apiAjaxGet(a,{},(function(e){0===e.code&&e.data&&(t.channelImage=e.data.filename&&r["a"].getImageUrl(e.data.filename),t.modalShown=!0,t.$forceUpdate())}),r["a"].defaultApiErrorHandler(a,""))}},loadDefaultParameters:function(){var t=this,e="algorithm/algorithmdefaultparameters/get_default/";c["a"].apiAjaxGet(e,{},(function(e){if(0===e.code)if(e.data.length>0){for(var a in t.defaultParameters={},u["a"].defaultAlgParams)t.defaultParameters[a]=e.data[0][a];for(var n in t.algStatus)t.algStatus[n].configured||Object.assign(t.algStatus[n],t.defaultParameters)}else t.defaultParameters=K({},u["a"].defaultAlgParams)}),r["a"].defaultApiErrorHandler(e,""))},loadAlgorithmChannels:function(t,e){var a=this,n="algorithm=".concat(this.currAlg.id);t&&(n="".concat(n,"&channel=").concat(t));var i="channel/channelalgorithms2/?".concat(n);c["a"].apiAjaxGet(i,{},(function(n){if(0===n.code){for(var i in a.channelStatusOld=Object(s["a"])(a.channelStatusOld),a.algStatus)t&&parseInt(i)!==e-1||(Object.assign(a.algStatus[i],K({configured:!1},a.defaultParameters)),a.channelStatusOld[i]=JSON.stringify(a.algStatus[i]));n.data.forEach((function(t){a.algStatus[t.channel.cno-1]=a.recordToStatus(t),a.channelStatusOld[t.channel.cno-1]=JSON.stringify(a.algStatus[t.channel.cno-1])})),a.$forceUpdate()}else console.log("获取通道算法失败！")}),r["a"].defaultApiErrorHandler(i,""))},loadChannels:function(){var t=this,e="channel/channels/";c["a"].apiAjaxGet(e,{},(function(e){if(0===e.code){for(var a in t.channelNames=new Array(z["a"].maxChannels).fill(""),t.channelIds=Object(s["a"])(t.channelIds),e.data)t.channelNames[e.data[a].cno-1]=e.data[a].name,t.channelIds[e.data[a].cno-1]=e.data[a].id;console.log("Channel loaded2",t.channelIds,t.channelNames)}}),r["a"].defaultApiErrorHandler(e,""))},currAlgChanged:function(){console.log("currAlgChanged",this.currAlg),this.loadChannels(),this.loadDefaultParameters(),this.loadAlgorithmChannels()},getCurrAlgByIndex:function(t){var e=Object.keys(this.algorithmInfo)[t];this.currAlg={id:this.algorithmInfo[e].id,name:e,name_ch:this.algorithmInfo[e].name_ch}},onStatusChanged:function(){var t=this;this.channelConfigured=this.algStatus.map((function(t){return t.configured})),this.channelStatusChanged=this.algStatus.map((function(e,a){return JSON.stringify(e)!==t.channelStatusOld[a]}))}},watch:{selectedCno:function(){console.log("selectedCno changed",this.selectedCno),this.loadChannelImage()},algStatus:{handler:function(){this.onStatusChanged()},deep:!0},channelStatusOld:function(){this.onStatusChanged()},channelIds:function(){console.log("channelIds",this.channelIds),this.loadChannelImage()},modalShown:function(){},currAlgIndex:function(){this.modalShown=!1,this.getCurrAlgByIndex(this.currAlgIndex),this.currAlgChanged()}},beforeUpdate:function(){this.updated||(this.updated=!0,window.currAlg?this.currAlg=K({},window.currAlg):this.getCurrAlgByIndex(0),this.currAlgIndex=Object.keys(this.algorithmInfo).indexOf(this.currAlg.name),this.currAlgChanged())},updated:function(){},beforeDestroy:function(){this.modalShown=!1},mounted:function(){}},Z=Q,tt=(a("3dba"),Object(D["a"])(Z,n,i,!1,null,null,null));e["default"]=tt.exports},"4d92":function(t,e,a){"use strict";var n=function(){var t=this,e=t._self._c;return e("div",[e("select",{directives:[{name:"model",rawName:"v-model",value:t.selected,expression:"selected"}],staticClass:"form-control font-iview-size control-sm",on:{change:function(e){var a=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.selected=e.target.multiple?a:a[0]}}},t._l(t.itemList,(function(a,n){return e("option",{key:t.uniqueId+n,domProps:{value:"item"===t.valueType?a:n}},[t._v(t._s("field"===t.showType?a[t.showField]:a))])})),0)])},i=[],s=a("fa7d"),l={name:"SimpleSelect",components:{},data:function(){return{uniqueId:s["a"].randomString(),selected:null}},props:{label:{type:String,required:!1,default:""},modelValue:{required:!1,default:-1},showType:{type:String,required:!1,default:"item"},valueType:{type:String,required:!1,default:"index"},showField:{type:String,required:!1,default:""},itemList:{type:Array,required:!0},required:{type:Boolean,required:!1,default:!1}},model:{prop:"modelValue",event:"input"},computed:{},methods:{},watch:{modelValue:function(){this.selected=this.modelValue},selected:function(){this.$emit("input",this.selected)}},mounted:function(){this.selected=this.modelValue},unmounted:function(){},created:function(){}},r=l,o=a("2877"),c=Object(o["a"])(r,n,i,!1,null,null,null);e["a"]=c.exports},5289:function(t,e,a){t.exports=a.p+"img/channel-configured.b36629f9.png"},"6c7b":function(t,e,a){var n=a("5ca1");n(n.P,"Array",{fill:a("36bd")}),a("9c6c")("fill")},"7bed":function(t,e,a){},"87ae":function(t,e,a){"use strict";a("b8e9")},b8e9:function(t,e,a){},c073:function(t,e,a){"use strict";a("c311")},c311:function(t,e,a){},c8da:function(t,e,a){"use strict";a("15b7")},cc1e:function(t,e,a){t.exports=a.p+"img/channel-not-configured.4da3f0ed.png"},cfd2:function(t,e,a){}}]);