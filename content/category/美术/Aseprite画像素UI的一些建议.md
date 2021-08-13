Title: Aseprite画像素UI的一些建议
Date: 2021-8-10
Modified: 2021-8-10
Category: 美术
Tags: Aseprite
Slug: Aseprite画像素UI的一些建议
Authors: Loop

* 使用一个大画布，把所有UI元素和图标都画在上面。
    * 打开背景网格作为尺寸参考，这样能够方便把握Sprite的大小，以及后续导入Unity后的Sprite切割（aseprite不支持单独切割Sprite并导出，只能整个画布一起导出）。
    * 从整体上把握UI风格，保持一致。例如：圆角还是尖角？阴影还是平面？ 3D 还是 2D？透视角度？
* 事先决定好需要的UI元素和图标，用清单把它们列出来。
    * 查看UI元素的网站：usability.gov。
* 使用垂直剖面线风格的阴影，不要使用抖动阴影（看起来会很脏）。
* 在Sprite下方使用较暗、冷色调的像素线来达到3D效果。
* 使用描边和阴影让UI和屏幕中的其他元素区分开来。
    * 描边和阴影不要使用纯黑或者灰色，应该根据Sprite的颜色而决定。
* 使用非像素UI作为参考，并把它们抽象出来形成像素画。
    * 参考图标的网站：flaticon.com。