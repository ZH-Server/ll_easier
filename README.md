# llbds_packer

一个用来打包指定版本的 带有 LeviLamina 的 Minecraft Bedrock Edition Server 的 GitAction 

## 如何食用?

首先以此仓库为模板在您的帐户下建立一个新仓库

然后打开 `Action` 页面

点击右侧的 `Pack LLBDS`

打开 `Run workflow` 填入你需要的 LeviLamina 版本号(在 LeviLamina 的 `Release` 页中查看可用版本)

点击 `Run workflow` 后，一杯白开水的功夫你就可以去 `Release` 里找到期待中的 `llbds_版本号.zip` 啦！

llbds_版本号.zip 解压后就是一个完整的带有 lip 环境的 LeviLamina + BDS 了

## 工作原理

在 GitAction 的服务器上先安装 lip ，之后利用 GitAction 的服务器“网速快”的“特性”，用 lip 安装 LeviLamina ，安装完成后再将其文件压缩为 llbds_版本号.zip 扔在 Release 中

## 有啥用?

新版的 LeviLamina 安装手动安装不是很简单迅速，用 lip 自动安装网络又不太好导致安装过程出现问题，所以有了这个仓库

## 有bug和建议?

提在 Issues 里，或交 PR 