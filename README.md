# LeviLamina Easier (Legacy手动)

**此仓库与 Mojang Studio 、 LiteDev 无关，本仓库只提供了非官方(Mojang Studio, LiteDev)构建的服务器打包，您使用本仓库进行构建说明您已经同意了 EULA 条款以及 LiteDev 颁发的许可证**

一个用于打包指定版本的 带有 LeviLamina 组件和环境 包的 Git Action

我们只希望以最高效、最方便的方式对 LeviLamina 进行安装

## 如何食用?

> 您可以调整所在分支位置至 `auto` 自动打包分支进行配置自动打包模式

首先以此仓库为模板在您的帐户下建立一个新仓库

然后打开 `Action` 页面

点击右侧的 `Pack LeviLamina`

打开 `Run workflow` 填入你需要的 LeviLamina 版本号(本 README 上的蓝色小标签中的数字)，以及按照个人需求填写其他内容

点击 `Run workflow` 后，一杯白开水的功夫你就可以去 `Release` 里找到期待中的 `ll_ll版本号_ll所需bds版本号.zip` 啦！

## 如何利用得到的压缩文件开服

先前往 [这里](https://www.minecraft.net/zh-hans/download/server/bedrock) 下载 所需版本 的 BDS 压缩包

> 如果发现版本在官方界面下载的与 Git Action 已经打包好的所需版本不一致，可以前往 [Minecraft Wiki](https://zh.minecraft.wiki/) 中查找所需版本，并下载服务器压缩文件

将下载好的 BDS 压缩文件解压在一个用于存储服务器文件的安全位置（以下简称 `BDS 根目录` ）

然后将 Git Action 打包好的压缩包文件解压在任意一个地方，然后将解压出的 `llbds` 字样文件夹里的东西全部移动至 `BDS 根目录`

双击运行 `PeEditor.exe` ，等待 `LeviLamina` 注入完成

最后，双击注入完成的 `bedrock_server_mod.exe`，成功开服！

## `Run workflow` 页中选项解释

| 名称          | 解释                      | 默认值        |
| ------------- | ------------------------- | ------------- |
| `LL_VER`      | `LeviLamina` 所需安装版本 | 0.1.0         |
| `LSE`         | 是否安装 `LSE`            | false         |
| `RUNTIME`     | 是否包括`LeviLamina`所需的C++运行时| false|
| `SCRIPTS`     | 是否运行仓库目录下的 `user_scripts.bat`|false|

> `SCRIPTS` 功能未经测试，出现任何问题后果自负！

-----

## 工作原理

在 Git Action 的服务器上先安装 lip ，之后利用 Git Action 的服务器“网速快”的“特性”，用 lip 安装 LeviLamina 之类，安装完成后再将其文件压缩并扔在 Release 中

## 有啥用?

新版的 LeviLamina 安装手动安装不是很简单，这对腐竹有一定技术要求；用 lip 自动安装网络又不太好导致安装过程出现各种奇怪问题，所以有了这个仓库以减轻开服难度

## 有Bug和建议?

提在 Issues/Discussion 里，或交 PR

什么？你说从 `Release` 中下载更慢？可以用一些镜像站嘛～

[镜像站1](https://moeyy.cn/gh-proxy)

[镜像站2](https://gh.lldc.top)

