(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-c298b13e"],{"0906":function(t,e,r){"use strict";r("505f")},"1da1":function(t,e,r){"use strict";function n(t,e,r,n,a,o,i){try{var s=t[o](i),u=s.value}catch(c){return void r(c)}s.done?e(u):Promise.resolve(u).then(n,a)}function a(t){return function(){var e=this,r=arguments;return new Promise((function(a,o){var i=t.apply(e,r);function s(t){n(i,a,o,s,u,"next",t)}function u(t){n(i,a,o,s,u,"throw",t)}s(void 0)}))}}r.d(e,"a",(function(){return a}))},"28c3":function(t,e,r){"use strict";r("b7fe")},"505f":function(t,e,r){},"69a0":function(t,e,r){(function(e){t.exports=e()})((function(t){"use strict";var e=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"];function r(t,e){var r=t[0],n=t[1],a=t[2],o=t[3];r+=(n&a|~n&o)+e[0]-680876936|0,r=(r<<7|r>>>25)+n|0,o+=(r&n|~r&a)+e[1]-389564586|0,o=(o<<12|o>>>20)+r|0,a+=(o&r|~o&n)+e[2]+606105819|0,a=(a<<17|a>>>15)+o|0,n+=(a&o|~a&r)+e[3]-1044525330|0,n=(n<<22|n>>>10)+a|0,r+=(n&a|~n&o)+e[4]-176418897|0,r=(r<<7|r>>>25)+n|0,o+=(r&n|~r&a)+e[5]+1200080426|0,o=(o<<12|o>>>20)+r|0,a+=(o&r|~o&n)+e[6]-1473231341|0,a=(a<<17|a>>>15)+o|0,n+=(a&o|~a&r)+e[7]-45705983|0,n=(n<<22|n>>>10)+a|0,r+=(n&a|~n&o)+e[8]+1770035416|0,r=(r<<7|r>>>25)+n|0,o+=(r&n|~r&a)+e[9]-1958414417|0,o=(o<<12|o>>>20)+r|0,a+=(o&r|~o&n)+e[10]-42063|0,a=(a<<17|a>>>15)+o|0,n+=(a&o|~a&r)+e[11]-1990404162|0,n=(n<<22|n>>>10)+a|0,r+=(n&a|~n&o)+e[12]+1804603682|0,r=(r<<7|r>>>25)+n|0,o+=(r&n|~r&a)+e[13]-40341101|0,o=(o<<12|o>>>20)+r|0,a+=(o&r|~o&n)+e[14]-1502002290|0,a=(a<<17|a>>>15)+o|0,n+=(a&o|~a&r)+e[15]+1236535329|0,n=(n<<22|n>>>10)+a|0,r+=(n&o|a&~o)+e[1]-165796510|0,r=(r<<5|r>>>27)+n|0,o+=(r&a|n&~a)+e[6]-1069501632|0,o=(o<<9|o>>>23)+r|0,a+=(o&n|r&~n)+e[11]+643717713|0,a=(a<<14|a>>>18)+o|0,n+=(a&r|o&~r)+e[0]-373897302|0,n=(n<<20|n>>>12)+a|0,r+=(n&o|a&~o)+e[5]-701558691|0,r=(r<<5|r>>>27)+n|0,o+=(r&a|n&~a)+e[10]+38016083|0,o=(o<<9|o>>>23)+r|0,a+=(o&n|r&~n)+e[15]-660478335|0,a=(a<<14|a>>>18)+o|0,n+=(a&r|o&~r)+e[4]-405537848|0,n=(n<<20|n>>>12)+a|0,r+=(n&o|a&~o)+e[9]+568446438|0,r=(r<<5|r>>>27)+n|0,o+=(r&a|n&~a)+e[14]-1019803690|0,o=(o<<9|o>>>23)+r|0,a+=(o&n|r&~n)+e[3]-187363961|0,a=(a<<14|a>>>18)+o|0,n+=(a&r|o&~r)+e[8]+1163531501|0,n=(n<<20|n>>>12)+a|0,r+=(n&o|a&~o)+e[13]-1444681467|0,r=(r<<5|r>>>27)+n|0,o+=(r&a|n&~a)+e[2]-51403784|0,o=(o<<9|o>>>23)+r|0,a+=(o&n|r&~n)+e[7]+1735328473|0,a=(a<<14|a>>>18)+o|0,n+=(a&r|o&~r)+e[12]-1926607734|0,n=(n<<20|n>>>12)+a|0,r+=(n^a^o)+e[5]-378558|0,r=(r<<4|r>>>28)+n|0,o+=(r^n^a)+e[8]-2022574463|0,o=(o<<11|o>>>21)+r|0,a+=(o^r^n)+e[11]+1839030562|0,a=(a<<16|a>>>16)+o|0,n+=(a^o^r)+e[14]-35309556|0,n=(n<<23|n>>>9)+a|0,r+=(n^a^o)+e[1]-1530992060|0,r=(r<<4|r>>>28)+n|0,o+=(r^n^a)+e[4]+1272893353|0,o=(o<<11|o>>>21)+r|0,a+=(o^r^n)+e[7]-155497632|0,a=(a<<16|a>>>16)+o|0,n+=(a^o^r)+e[10]-1094730640|0,n=(n<<23|n>>>9)+a|0,r+=(n^a^o)+e[13]+681279174|0,r=(r<<4|r>>>28)+n|0,o+=(r^n^a)+e[0]-358537222|0,o=(o<<11|o>>>21)+r|0,a+=(o^r^n)+e[3]-722521979|0,a=(a<<16|a>>>16)+o|0,n+=(a^o^r)+e[6]+76029189|0,n=(n<<23|n>>>9)+a|0,r+=(n^a^o)+e[9]-640364487|0,r=(r<<4|r>>>28)+n|0,o+=(r^n^a)+e[12]-421815835|0,o=(o<<11|o>>>21)+r|0,a+=(o^r^n)+e[15]+530742520|0,a=(a<<16|a>>>16)+o|0,n+=(a^o^r)+e[2]-995338651|0,n=(n<<23|n>>>9)+a|0,r+=(a^(n|~o))+e[0]-198630844|0,r=(r<<6|r>>>26)+n|0,o+=(n^(r|~a))+e[7]+1126891415|0,o=(o<<10|o>>>22)+r|0,a+=(r^(o|~n))+e[14]-1416354905|0,a=(a<<15|a>>>17)+o|0,n+=(o^(a|~r))+e[5]-57434055|0,n=(n<<21|n>>>11)+a|0,r+=(a^(n|~o))+e[12]+1700485571|0,r=(r<<6|r>>>26)+n|0,o+=(n^(r|~a))+e[3]-1894986606|0,o=(o<<10|o>>>22)+r|0,a+=(r^(o|~n))+e[10]-1051523|0,a=(a<<15|a>>>17)+o|0,n+=(o^(a|~r))+e[1]-2054922799|0,n=(n<<21|n>>>11)+a|0,r+=(a^(n|~o))+e[8]+1873313359|0,r=(r<<6|r>>>26)+n|0,o+=(n^(r|~a))+e[15]-30611744|0,o=(o<<10|o>>>22)+r|0,a+=(r^(o|~n))+e[6]-1560198380|0,a=(a<<15|a>>>17)+o|0,n+=(o^(a|~r))+e[13]+1309151649|0,n=(n<<21|n>>>11)+a|0,r+=(a^(n|~o))+e[4]-145523070|0,r=(r<<6|r>>>26)+n|0,o+=(n^(r|~a))+e[11]-1120210379|0,o=(o<<10|o>>>22)+r|0,a+=(r^(o|~n))+e[2]+718787259|0,a=(a<<15|a>>>17)+o|0,n+=(o^(a|~r))+e[9]-343485551|0,n=(n<<21|n>>>11)+a|0,t[0]=r+t[0]|0,t[1]=n+t[1]|0,t[2]=a+t[2]|0,t[3]=o+t[3]|0}function n(t){var e,r=[];for(e=0;e<64;e+=4)r[e>>2]=t.charCodeAt(e)+(t.charCodeAt(e+1)<<8)+(t.charCodeAt(e+2)<<16)+(t.charCodeAt(e+3)<<24);return r}function a(t){var e,r=[];for(e=0;e<64;e+=4)r[e>>2]=t[e]+(t[e+1]<<8)+(t[e+2]<<16)+(t[e+3]<<24);return r}function o(t){var e,a,o,i,s,u,c=t.length,l=[1732584193,-271733879,-1732584194,271733878];for(e=64;e<=c;e+=64)r(l,n(t.substring(e-64,e)));for(t=t.substring(e-64),a=t.length,o=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],e=0;e<a;e+=1)o[e>>2]|=t.charCodeAt(e)<<(e%4<<3);if(o[e>>2]|=128<<(e%4<<3),e>55)for(r(l,o),e=0;e<16;e+=1)o[e]=0;return i=8*c,i=i.toString(16).match(/(.*?)(.{0,8})$/),s=parseInt(i[2],16),u=parseInt(i[1],16)||0,o[14]=s,o[15]=u,r(l,o),l}function i(t){var e,n,o,i,s,u,c=t.length,l=[1732584193,-271733879,-1732584194,271733878];for(e=64;e<=c;e+=64)r(l,a(t.subarray(e-64,e)));for(t=e-64<c?t.subarray(e-64):new Uint8Array(0),n=t.length,o=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],e=0;e<n;e+=1)o[e>>2]|=t[e]<<(e%4<<3);if(o[e>>2]|=128<<(e%4<<3),e>55)for(r(l,o),e=0;e<16;e+=1)o[e]=0;return i=8*c,i=i.toString(16).match(/(.*?)(.{0,8})$/),s=parseInt(i[2],16),u=parseInt(i[1],16)||0,o[14]=s,o[15]=u,r(l,o),l}function s(t){var r,n="";for(r=0;r<4;r+=1)n+=e[t>>8*r+4&15]+e[t>>8*r&15];return n}function u(t){var e;for(e=0;e<t.length;e+=1)t[e]=s(t[e]);return t.join("")}function c(t){return/[\u0080-\uFFFF]/.test(t)&&(t=unescape(encodeURIComponent(t))),t}function l(t,e){var r,n=t.length,a=new ArrayBuffer(n),o=new Uint8Array(a);for(r=0;r<n;r+=1)o[r]=t.charCodeAt(r);return e?o:a}function f(t){return String.fromCharCode.apply(null,new Uint8Array(t))}function h(t,e,r){var n=new Uint8Array(t.byteLength+e.byteLength);return n.set(new Uint8Array(t)),n.set(new Uint8Array(e),t.byteLength),r?n:n.buffer}function d(t){var e,r=[],n=t.length;for(e=0;e<n-1;e+=2)r.push(parseInt(t.substr(e,2),16));return String.fromCharCode.apply(String,r)}function p(){this.reset()}return"5d41402abc4b2a76b9719d911017c592"!==u(o("hello"))&&function(t,e){var r=(65535&t)+(65535&e),n=(t>>16)+(e>>16)+(r>>16);return n<<16|65535&r},"undefined"===typeof ArrayBuffer||ArrayBuffer.prototype.slice||function(){function e(t,e){return t=0|t||0,t<0?Math.max(t+e,0):Math.min(t,e)}ArrayBuffer.prototype.slice=function(r,n){var a,o,i,s,u=this.byteLength,c=e(r,u),l=u;return n!==t&&(l=e(n,u)),c>l?new ArrayBuffer(0):(a=l-c,o=new ArrayBuffer(a),i=new Uint8Array(o),s=new Uint8Array(this,c,a),i.set(s),o)}}(),p.prototype.append=function(t){return this.appendBinary(c(t)),this},p.prototype.appendBinary=function(t){this._buff+=t,this._length+=t.length;var e,a=this._buff.length;for(e=64;e<=a;e+=64)r(this._hash,n(this._buff.substring(e-64,e)));return this._buff=this._buff.substring(e-64),this},p.prototype.end=function(t){var e,r,n=this._buff,a=n.length,o=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];for(e=0;e<a;e+=1)o[e>>2]|=n.charCodeAt(e)<<(e%4<<3);return this._finish(o,a),r=u(this._hash),t&&(r=d(r)),this.reset(),r},p.prototype.reset=function(){return this._buff="",this._length=0,this._hash=[1732584193,-271733879,-1732584194,271733878],this},p.prototype.getState=function(){return{buff:this._buff,length:this._length,hash:this._hash.slice()}},p.prototype.setState=function(t){return this._buff=t.buff,this._length=t.length,this._hash=t.hash,this},p.prototype.destroy=function(){delete this._hash,delete this._buff,delete this._length},p.prototype._finish=function(t,e){var n,a,o,i=e;if(t[i>>2]|=128<<(i%4<<3),i>55)for(r(this._hash,t),i=0;i<16;i+=1)t[i]=0;n=8*this._length,n=n.toString(16).match(/(.*?)(.{0,8})$/),a=parseInt(n[2],16),o=parseInt(n[1],16)||0,t[14]=a,t[15]=o,r(this._hash,t)},p.hash=function(t,e){return p.hashBinary(c(t),e)},p.hashBinary=function(t,e){var r=o(t),n=u(r);return e?d(n):n},p.ArrayBuffer=function(){this.reset()},p.ArrayBuffer.prototype.append=function(t){var e,n=h(this._buff.buffer,t,!0),o=n.length;for(this._length+=t.byteLength,e=64;e<=o;e+=64)r(this._hash,a(n.subarray(e-64,e)));return this._buff=e-64<o?new Uint8Array(n.buffer.slice(e-64)):new Uint8Array(0),this},p.ArrayBuffer.prototype.end=function(t){var e,r,n=this._buff,a=n.length,o=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];for(e=0;e<a;e+=1)o[e>>2]|=n[e]<<(e%4<<3);return this._finish(o,a),r=u(this._hash),t&&(r=d(r)),this.reset(),r},p.ArrayBuffer.prototype.reset=function(){return this._buff=new Uint8Array(0),this._length=0,this._hash=[1732584193,-271733879,-1732584194,271733878],this},p.ArrayBuffer.prototype.getState=function(){var t=p.prototype.getState.call(this);return t.buff=f(t.buff),t},p.ArrayBuffer.prototype.setState=function(t){return t.buff=l(t.buff,!0),p.prototype.setState.call(this,t)},p.ArrayBuffer.prototype.destroy=p.prototype.destroy,p.ArrayBuffer.prototype._finish=p.prototype._finish,p.ArrayBuffer.hash=function(t,e){var r=i(new Uint8Array(t)),n=u(r);return e?d(n):n},p}))},"96cf":function(t,e,r){var n=function(t){"use strict";var e,r=Object.prototype,n=r.hasOwnProperty,a="function"===typeof Symbol?Symbol:{},o=a.iterator||"@@iterator",i=a.asyncIterator||"@@asyncIterator",s=a.toStringTag||"@@toStringTag";function u(t,e,r){return Object.defineProperty(t,e,{value:r,enumerable:!0,configurable:!0,writable:!0}),t[e]}try{u({},"")}catch(T){u=function(t,e,r){return t[e]=r}}function c(t,e,r,n){var a=e&&e.prototype instanceof y?e:y,o=Object.create(a.prototype),i=new F(n||[]);return o._invoke=U(t,r,i),o}function l(t,e,r){try{return{type:"normal",arg:t.call(e,r)}}catch(T){return{type:"throw",arg:T}}}t.wrap=c;var f="suspendedStart",h="suspendedYield",d="executing",p="completed",g={};function y(){}function m(){}function v(){}var w={};u(w,o,(function(){return this}));var b=Object.getPrototypeOf,_=b&&b(b(L([])));_&&_!==r&&n.call(_,o)&&(w=_);var S=v.prototype=y.prototype=Object.create(w);function C(t){["next","throw","return"].forEach((function(e){u(t,e,(function(t){return this._invoke(e,t)}))}))}function x(t,e){function r(a,o,i,s){var u=l(t[a],t,o);if("throw"!==u.type){var c=u.arg,f=c.value;return f&&"object"===typeof f&&n.call(f,"__await")?e.resolve(f.__await).then((function(t){r("next",t,i,s)}),(function(t){r("throw",t,i,s)})):e.resolve(f).then((function(t){c.value=t,i(c)}),(function(t){return r("throw",t,i,s)}))}s(u.arg)}var a;function o(t,n){function o(){return new e((function(e,a){r(t,n,e,a)}))}return a=a?a.then(o,o):o()}this._invoke=o}function U(t,e,r){var n=f;return function(a,o){if(n===d)throw new Error("Generator is already running");if(n===p){if("throw"===a)throw o;return j()}r.method=a,r.arg=o;while(1){var i=r.delegate;if(i){var s=k(i,r);if(s){if(s===g)continue;return s}}if("next"===r.method)r.sent=r._sent=r.arg;else if("throw"===r.method){if(n===f)throw n=p,r.arg;r.dispatchException(r.arg)}else"return"===r.method&&r.abrupt("return",r.arg);n=d;var u=l(t,e,r);if("normal"===u.type){if(n=r.done?p:h,u.arg===g)continue;return{value:u.arg,done:r.done}}"throw"===u.type&&(n=p,r.method="throw",r.arg=u.arg)}}}function k(t,r){var n=t.iterator[r.method];if(n===e){if(r.delegate=null,"throw"===r.method){if(t.iterator["return"]&&(r.method="return",r.arg=e,k(t,r),"throw"===r.method))return g;r.method="throw",r.arg=new TypeError("The iterator does not provide a 'throw' method")}return g}var a=l(n,t.iterator,r.arg);if("throw"===a.type)return r.method="throw",r.arg=a.arg,r.delegate=null,g;var o=a.arg;return o?o.done?(r[t.resultName]=o.value,r.next=t.nextLoc,"return"!==r.method&&(r.method="next",r.arg=e),r.delegate=null,g):o:(r.method="throw",r.arg=new TypeError("iterator result is not an object"),r.delegate=null,g)}function A(t){var e={tryLoc:t[0]};1 in t&&(e.catchLoc=t[1]),2 in t&&(e.finallyLoc=t[2],e.afterLoc=t[3]),this.tryEntries.push(e)}function I(t){var e=t.completion||{};e.type="normal",delete e.arg,t.completion=e}function F(t){this.tryEntries=[{tryLoc:"root"}],t.forEach(A,this),this.reset(!0)}function L(t){if(t){var r=t[o];if(r)return r.call(t);if("function"===typeof t.next)return t;if(!isNaN(t.length)){var a=-1,i=function r(){while(++a<t.length)if(n.call(t,a))return r.value=t[a],r.done=!1,r;return r.value=e,r.done=!0,r};return i.next=i}}return{next:j}}function j(){return{value:e,done:!0}}return m.prototype=v,u(S,"constructor",v),u(v,"constructor",m),m.displayName=u(v,s,"GeneratorFunction"),t.isGeneratorFunction=function(t){var e="function"===typeof t&&t.constructor;return!!e&&(e===m||"GeneratorFunction"===(e.displayName||e.name))},t.mark=function(t){return Object.setPrototypeOf?Object.setPrototypeOf(t,v):(t.__proto__=v,u(t,s,"GeneratorFunction")),t.prototype=Object.create(S),t},t.awrap=function(t){return{__await:t}},C(x.prototype),u(x.prototype,i,(function(){return this})),t.AsyncIterator=x,t.async=function(e,r,n,a,o){void 0===o&&(o=Promise);var i=new x(c(e,r,n,a),o);return t.isGeneratorFunction(r)?i:i.next().then((function(t){return t.done?t.value:i.next()}))},C(S),u(S,s,"Generator"),u(S,o,(function(){return this})),u(S,"toString",(function(){return"[object Generator]"})),t.keys=function(t){var e=[];for(var r in t)e.push(r);return e.reverse(),function r(){while(e.length){var n=e.pop();if(n in t)return r.value=n,r.done=!1,r}return r.done=!0,r}},t.values=L,F.prototype={constructor:F,reset:function(t){if(this.prev=0,this.next=0,this.sent=this._sent=e,this.done=!1,this.delegate=null,this.method="next",this.arg=e,this.tryEntries.forEach(I),!t)for(var r in this)"t"===r.charAt(0)&&n.call(this,r)&&!isNaN(+r.slice(1))&&(this[r]=e)},stop:function(){this.done=!0;var t=this.tryEntries[0],e=t.completion;if("throw"===e.type)throw e.arg;return this.rval},dispatchException:function(t){if(this.done)throw t;var r=this;function a(n,a){return s.type="throw",s.arg=t,r.next=n,a&&(r.method="next",r.arg=e),!!a}for(var o=this.tryEntries.length-1;o>=0;--o){var i=this.tryEntries[o],s=i.completion;if("root"===i.tryLoc)return a("end");if(i.tryLoc<=this.prev){var u=n.call(i,"catchLoc"),c=n.call(i,"finallyLoc");if(u&&c){if(this.prev<i.catchLoc)return a(i.catchLoc,!0);if(this.prev<i.finallyLoc)return a(i.finallyLoc)}else if(u){if(this.prev<i.catchLoc)return a(i.catchLoc,!0)}else{if(!c)throw new Error("try statement without catch or finally");if(this.prev<i.finallyLoc)return a(i.finallyLoc)}}}},abrupt:function(t,e){for(var r=this.tryEntries.length-1;r>=0;--r){var a=this.tryEntries[r];if(a.tryLoc<=this.prev&&n.call(a,"finallyLoc")&&this.prev<a.finallyLoc){var o=a;break}}o&&("break"===t||"continue"===t)&&o.tryLoc<=e&&e<=o.finallyLoc&&(o=null);var i=o?o.completion:{};return i.type=t,i.arg=e,o?(this.method="next",this.next=o.finallyLoc,g):this.complete(i)},complete:function(t,e){if("throw"===t.type)throw t.arg;return"break"===t.type||"continue"===t.type?this.next=t.arg:"return"===t.type?(this.rval=this.arg=t.arg,this.method="return",this.next="end"):"normal"===t.type&&e&&(this.next=e),g},finish:function(t){for(var e=this.tryEntries.length-1;e>=0;--e){var r=this.tryEntries[e];if(r.finallyLoc===t)return this.complete(r.completion,r.afterLoc),I(r),g}},catch:function(t){for(var e=this.tryEntries.length-1;e>=0;--e){var r=this.tryEntries[e];if(r.tryLoc===t){var n=r.completion;if("throw"===n.type){var a=n.arg;I(r)}return a}}throw new Error("illegal catch attempt")},delegateYield:function(t,r,n){return this.delegate={iterator:L(t),resultName:r,nextLoc:n},"next"===this.method&&(this.arg=e),g}},t}(t.exports);try{regeneratorRuntime=n}catch(a){"object"===typeof globalThis?globalThis.regeneratorRuntime=n:Function("r","regeneratorRuntime = r")(n)}},b7fe:function(t,e,r){},bea8:function(t,e,r){"use strict";r.r(e);var n=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[e("div",{staticClass:"col-lg-4 col-md-6"},[e("div",{staticClass:"card w-100"},[t._m(0),e("div",{staticClass:"card-body py-1 px-2 col upgrade-panel-block"},[e("button",{staticClass:"btn btn-primary btn-sm btn-iview-size",attrs:{disabled:t.upgradeStarted,"data-toggle":"modal","data-target":"#"+t.networkUpgradeConfirmDlgId}},[t._v(t._s(t.upgradeStarted?"升级中，请耐心等候...":"开始升级"))])])])]),e("div",{staticClass:"col-lg-4 col-md-6"},[e("div",{staticClass:"card w-100"},[t._m(1),e("div",{staticClass:"card-body py-1 px-2 col upgrade-panel-block"},[e("UpgradeFileUpload",{attrs:{networkUpgradeStarted:t.networkUpgradeStarted},on:{"upgrade-started":t.onManualUpgradeStarted}})],1)])])]),e("SystemUpgradeConfirmDlg",{attrs:{modalId:t.networkUpgradeConfirmDlgId},on:{"upgrade-started":t.onNetworkUpgradeStarted}})],1)},a=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"card-header py-1 px-2 dash-chart-title"},[e("span",{staticClass:"card-head-title"},[t._v("网络自动升级")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"card-header py-1 px-2 dash-chart-title"},[e("span",{staticClass:"card-head-title"},[t._v("本地手动升级")])])}],o=r("fa7d"),i=function(){var t=this,e=t._self._c;return e("div",[e("SimpleModalDlg",{attrs:{modalId:t.modalId,title:"系统升级",content:"",defaultButtonText:"取消",button2Text:"确认",button2Action:t.button2Action,dialogWidth:500},scopedSlots:t._u([{key:"bodyPost",fn:function(){return[e("IconFont",{staticStyle:{"font-size":"2em",color:"rgb(255, 186, 0)"},attrs:{iconName:"icon-tanhao"}}),t._v("\n    根据网络状况，升级将会花费5分钟到30分钟时间。请确认设备已经联网，并且能正常访问互联网。如果不能访问互联网，请选择本地升级。\n  ")]},proxy:!0}])}),e("Toast",{attrs:{toastId:t.toastId,text:"升级开始"}})],1)},s=[],u=r("f953"),c=r("0be2"),l=r("8cbb"),f={name:"SystemUpgradeConfirmDlg",components:{SimpleModalDlg:u["a"]},data:function(){return{toastId:o["a"].randomId("toast")}},props:{modalId:{type:String,required:!0}},computed:{},methods:{button2Action:function(){var t=this,e="system/projectinfos/start_upgrade/",r={};c["a"].apiAjaxPost(e,r,(function(){l["a"].showToast(t.toastId),t.$emit("upgrade-started")}),o["a"].defaultApiErrorHandler(e,""))}},watch:{},mounted:function(){}},h=f,d=r("2877"),p=Object(d["a"])(h,i,s,!1,null,null,null),g=p.exports,y=function(){var t=this,e=t._self._c;return e("div",{staticClass:"w-100 multi-upload-control"},[e("div",{staticClass:"row mt-3"},[e("div",{staticClass:"col"},[e("span",{staticClass:"field-label-non-bold"},[t._v("上传进度：")]),e("div",{staticClass:"progress w-100 mt-2"},[e("div",{staticClass:"progress-bar progress-bar-striped progress-bar-animated",style:"width: ".concat(t.progressPercent,"%;"),attrs:{id:t.progressId,role:"progressbar","aria-valuenow":t.progressValuenow,"aria-valuemin":t.progressValuemin,"aria-valuemax":t.progressValuemax}},[t._v("\n              "+t._s(t.progressPercent)+"%\n          ")])])])]),e("div",{staticClass:"row mt-3"},[e("div",{staticClass:"col"},[e("span",{staticClass:"field-label-non-bold"},[t._v("文件名：")]),e("input",{staticClass:"form-control",staticStyle:{"max-width":"100%",width:"100em","font-size":"0.75em"},attrs:{type:"text"},domProps:{value:t.filename}})])]),e("br"),e("button",{staticClass:"btn btn-sm btn-primary",attrs:{disabled:t.upgradeStarted||t.loadingFile},on:{click:t.onSelectFile}},[t._v("选择文件")]),e("button",{staticClass:"btn btn-sm btn-primary ml-2",attrs:{disabled:t.upgradeStarted||!t.fileRaw||t.loadingFile},on:{click:t.onUploadFile}},[t._v(t._s(t.loadingFile?"文件上传中...":"上传文件"))]),e("button",{staticClass:"btn btn-sm btn-primary ml-2",attrs:{disabled:t.upgradeStarted||t.loadingFile||!t.uploadSuccess||t.upgradeStarted},on:{click:t.onStartUpgade}},[t._v(t._s(t.upgradeStarted?"升级中，请耐心等候...":"开始升级"))]),e("input",{staticStyle:{display:"none"},attrs:{type:"file",name:"filenames",id:t.fileInputId,accept:t.accept},on:{change:t.onFilesChange}}),e("Toast",{attrs:{toastId:t.toastId,text:t.toastText}}),e("SimpleModalDlg",{attrs:{modalId:t.alertModalId,content:t.alertConent,title:t.alertTitle,defaultButtonText:"确认"}})],1)},m=[],v=(r("96cf"),r("1da1")),w=(r("7f7f"),r("69a0")),b=r.n(w),_=r("bc3a"),S=r.n(_),C=r("5f87"),x=10485760,U={name:"UpgradeFileUpload",components:{},data:function(){return{loadingFile:!1,alertModalId:o["a"].randomId("modal"),alertConent:"",alertTitle:"",toastId:o["a"].randomId("toast"),fileInputId:o["a"].randomId("button"),progressId:o["a"].randomId("progress"),progressValuenow:0,progressValuemin:0,progressValuemax:1e3,progressPercent:0,buttonDisabled:!1,accept:"*/*",toastText:"Toast",fileRaw:null,uploadSuccess:!1,manualUpgradeStarted:!1}},props:{networkUpgradeStarted:{type:Boolean,required:!0}},computed:{filename:function(){return this.fileRaw&&this.fileRaw.name||""},upgradeStarted:function(){return this.manualUpgradeStarted||this.networkUpgradeStarted}},methods:{showAlert:function(t,e){this.alertTitle=t,this.alertConent=e,u["a"].show(this.alertModalId)},onSelectFile:function(){$("#".concat(this.fileInputId)).trigger("click")},startUpgade:function(){var t=this,e="system/projectinfos/start_upgrade_manual/",r={filename:this.fileRaw.name};c["a"].apiAjaxPost(e,r,(function(e){0===e.code?(t.manualUpgradeStarted=!0,t.showToast("开始升级"),t.$emit("upgrade-started",t.fileRaw.name)):t.showAlert("升级失败","升级失败，可能是文件上传错误！")}),(function(e){t.showAlert("启动升级失败，请重试",JSON.stringify(e))}))},onStartUpgade:function(){var t=Object(v["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:this.startUpgade();case 1:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}(),onFilesChange:function(){var t=Object(v["a"])(regeneratorRuntime.mark((function t(){var e;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:e=document.getElementById(this.fileInputId),e.files.length>0&&(this.fileRaw=e.files[0]);case 2:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}(),onUploadFile:function(){var t=Object(v["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:this.uploadFile({raw:this.fileRaw,size:this.fileRaw.size,name:this.fileRaw.name});case 1:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}(),showToast:function(t){this.toastText=t,l["a"].showToast(this.toastId)},uploadDone:function(t){this.loadingFile=!1,this.showToast("上传成功"),this.uploadSuccess=!0},updateProgress:function(t,e){this.progressValuenow=Math.round(e*this.progressValuemax/t.totalChunks),this.progressPercent=Math.round(100*e/t.totalChunks)},uploadFile:function(){var t=Object(v["a"])(regeneratorRuntime.mark((function t(e){var r,n,a,o=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:this.loadingFile=!0,r=e.raw,this.currentFile=r,n=e.size,a=Math.ceil(n/x),console.log("文件大小：",e.size/1024/1024+"Mb","分片数：",a),this.getFileMd5(r,a).then((function(t){var r={identifier:t,filename:e.name,totalChunks:a};c["a"].apiAjaxPost("/upload/uploads/check_chunk_exist/",r,(function(t){!0===t.data.allUploadSuccess&&!0===t.data.mergeSuccess?(o.updateProgress(r,r.totalChunks),o.uploadDone(!0)):o.uploadChunk(e,r,t.data.uploaded)}))}));case 8:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}(),uploadChunk:function(t,e,r){var n=this,a=r;console.log(a,"分片开始序号"),this.updateProgress(e,a);var o=e.identifier;if(a!==e.totalChunks){var i=a,s=i*x,u=Math.min(t.size,s+x),c=t.raw.slice(s,u),l=new FormData;l.append("identifier",o),l.append("filename",t.name),l.append("totalChunks",e.totalChunks),l.append("chunkNumber",i),l.append("totalSize",t.size),l.append("file_field",c),S()({method:"post",url:"/api/v1/upload/uploads/chunk/",data:l,headers:{Authorization:"Token ".concat(Object(C["f"])())},transformRequest:[function(t,e){return delete e.post["Content-Type"],t}]}).then((function(r){0===r.code?n.uploadChunk(t,e,r.data.data.uploaded):n.showAlert("文件上传失败","上传失败：".concat(r.message,"。请重试"))})).catch((function(t){console.log("file chunk upload error",t,l),n.showAlert("上传失败，请重试",JSON.stringify(t))}))}else this.composeFile(e)},getFileMd5:function(t,e){return new Promise((function(r,n){var a=File.prototype.slice||File.prototype.mozSlice||File.prototype.webkitSlice,o=e,i=0,s=new b.a.ArrayBuffer,u=new FileReader;function c(){var e=i*x,r=e+x;r>t.size&&(r=t.size),u.readAsArrayBuffer(a.call(t,e,r))}u.onload=function(t){if(s.append(t.target.result),i++,i<o)c();else{var e=s.end();r(e)}},u.onerror=function(t){n(t)},c()}))},composeFile:function(t){var e=this;c["a"].apiAjaxPost("/upload/uploads/merge/",t,(function(t){0==t.code?e.uploadDone(!1):(e.loadingFile=!1,e.showAlert("文件上传失败，请重试！",t.message))}),(function(t){e.showAlert("文件上传失败，请重试！",JSON.stringify(t))}))}},created:function(){},mounted:function(){}},k=U,A=(r("28c3"),Object(d["a"])(k,y,m,!1,null,null,null)),I=A.exports,F={name:"SysConfigRestartDevice",components:{SystemUpgradeConfirmDlg:g,UpgradeFileUpload:I},data:function(){return{networkUpgradeConfirmDlgId:o["a"].randomId("modal"),localUpgradeConfirmDlgId:o["a"].randomId("modal"),networkUpgradeStarted:!1,manualUpgradeStarted:!1,apis:c["a"]}},computed:{upgradeStarted:function(){return this.manualUpgradeStarted||this.networkUpgradeStarted}},methods:{resetDone:function(t){t.networkUpgradeStarted=!1},checkUpgradeDone:function(t){console.log("checkUpgradeDone",t);var e="system/projectinfos/get_device_info/";t.apis.apiAjaxGet(e,{},(function(){t.resetDone(t)}),(function(){setTimeout((function(){t.checkUpgradeDone(t)}),5e3)}))},onUpgradeStarted:function(){var t=this,e=this;setTimeout((function(){t.checkUpgradeDone(e)}),3e5)},onNetworkUpgradeStarted:function(){console.log("networkUpgradeStarted",this),this.networkUpgradeStarted=!0,this.onUpgradeStarted()},onManualUpgradeStarted:function(){console.log("manualUpgradeStarted",this),this.manualUpgradeStarted=!0,this.onUpgradeStarted()}}},L=F,j=(r("0906"),Object(d["a"])(L,n,a,!1,null,null,null));e["default"]=j.exports}}]);