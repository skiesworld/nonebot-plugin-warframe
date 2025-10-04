# nonebot-plugin-warframe

基于NoneBot的星际战甲事件查询插件

## 前置

插件含有 `match` 语法，请在 `Python 3.10` 或更高版本运行

## 安装

### 使用 pip

```shell
pip install nonebot-plugin-warframe
```

### 使用 uv（推荐）

1. 安装 uv（如果尚未安装）

  PowerShell:

  ```powershell
  pip install uv
  ```

  可选官方安装脚本：

  ```powershell
  powershell -ExecutionPolicy Bypass -c "iwr https://astral.sh/install.ps1 -useb | iex"
  ```

1. 在你的 NoneBot 项目根目录添加插件依赖：

  ```powershell
  uv add nonebot-plugin-warframe
  ```

  如果你的项目还没有 `pyproject.toml`，先初始化：

  ```powershell
  uv init
  uv add nonebot-plugin-warframe
  ```

1. 运行 NoneBot：

  ```powershell
  uv run nb run
  ```

### NoneBot2 插件商店

```shell
nb plugin install nonebot-plugin-warframe
```

## 使用

- 命令头：`wf`、`warframe`、`星际战甲`
- 菜单：`wf 菜单`

```text
命令头：wf、warframe、星际战甲
参数：
==================
警报丨入侵丨赏金丨突击丨裂隙
章节丨地球丨赛特斯丨索拉里斯
奸商丨事件丨新闻丨每日优惠
```

## 特别感谢

- [NoneBot2](https://github.com/nonebot/nonebot2)： 插件使用的开发框架。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)： 稳定完善的 CQHTTP 实现。
- [奥迪斯](https://ordis.null00.com/v1/)：星际战甲国服API
