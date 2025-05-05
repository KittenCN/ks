## 项目简介  
这里是[CoderFAN](https://www.coderfan.com)的资料库, 主要用于编程学习资料的收集和分享。  
如需要进一步学习编程知识，可以访问 *[OJ学习平台](https://www.coderfan.com)* 。  

>本项目有2个不同的镜像站点，分别是：
>>[静态主站](https://wiki.coderfan.com)  
>>[GitHub镜像站](https://kittencn.github.io/ks/_book/)  
>>请按需要，请自行选择。  
>如有任何问题，请联系[CoderFAN](https://www.coderfan.com)的站长。

## 项目拓展
原始项目是基于Docsify的轻量eBook，但是其特性导致不能很好的兼容各种搜索引擎的SEO，且SSR插件问题很多，因此同步迁移/部署到honkit/gitbook中。
为此，我写了几个配合迁移的python脚本，有兴趣的可以修改使用：
1. [split_vol.py](https://github.com/KittenCN/ks/blob/master/split_vol.py) : 该脚本可以通过SUMMARY.md文件读取文档结构，然后按照结构层次重新分配到各个子目录中，从而将很大的文档拆解为若干子文档，能极大的提高honkit/gitbook解析速度。
2. [build_all.py](https://github.com/KittenCN/ks/blob/master/build_all.py) : 能够使用多线程解析编译md文档为html文件，且按照从根到枝的顺序进行有序排列，能极大的提高honkit/gitbook解析速度。

## 内容简介
本项目主要包括以下内容 (本项目部分内容借用了[xflihaibo](https://xflihaibo.github.io/docs/)的基础数据，感谢！)：  
1. [开发规范](standard/README.md) ：包括各种开发过程中应遵守的通用规则  
2. [前端汇总](web/README.md) ：包括前端开发过程中常用的各种技术和工具  
3. [后端汇总](coding/README.md) ：包括后端开发过程中常用的各种技术和工具  
4. [算法汇总](algorithms/README.md) ：包括基础算法学习资料,这些都是程序员必备的技能。感谢大佬[krahets](https://github.com/krahets/hello-algo)。  
5. [AP课程](ap/README.md) ：包括AP课程学习资料及部分历史真题  
6. [数学知识](math/README.md) ：程序员都应该了解的数学知识  
7. [工具集合](tool/README.md) ：包括各种开发过程中常用的工具  
8. [进阶知识](advance/README.md) ：包括各种进阶知识  
9. [资料下载](docs/README.md)   ：包括各种学习资料的下载  
[![img](img/coderfan_logo.png)](https://www.coderfan.com) 
