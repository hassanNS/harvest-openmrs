var __bind=function(t,o){return function(){return t.apply(o,arguments)}},__hasProp={}.hasOwnProperty,__extends=function(t,o){function e(){this.constructor=t}for(var n in o)__hasProp.call(o,n)&&(t[n]=o[n]);return e.prototype=o.prototype,t.prototype=new e,t.__super__=o.prototype,t};define(["underscore","marionette","./row"],function(t,o,e){var n;return n=function(o){function n(){return this.itemViewOptions=__bind(this.itemViewOptions,this),n.__super__.constructor.apply(this,arguments)}return __extends(n,o),n.prototype.tagName="tbody",n.prototype.template=function(){},n.prototype.itemView=e.Row,n.prototype.itemViewOptions=function(o){return t.defaults({collection:o.data},this.options)},n}(o.CollectionView),{Body:n}});
//# sourceMappingURL=body.js.map