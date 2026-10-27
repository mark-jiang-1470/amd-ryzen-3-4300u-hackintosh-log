# AMD Ryzen 3 4300U 黑苹果日志

记录这台 AMD Renoir 机器安装与维护 macOS Tahoe 的真实硬件、脱敏 EFI、配置改动、驱动选择和未解决问题，供相近平台参考。

**核验日期：2026-10-28。** EFI 来源为当前内置分区的只读实拷贝，源配置与最后安装收据一致；公开版已清除机器身份、通过 OpenCore 1.0.9 的 `ocvalidate`，未用公开副本重新启动验收。不是适用所有 Ryzen 电脑的通用包。

| 部件 | 本机配置 |
|---|---|
| CPU | AMD Ryzen 3 4300U，Renoir / Zen 2，4 核 4 线程；官方基础/最高加速 2.7/3.7GHz，标称 TDP 15W |
| 内存 | 16GB，海力士 8GB × 2，DDR4；系统 SPD 报告 2400MHz |
| 核显 | Radeon Vega 5 / Renoir，PCI 1002:1636，系统报告共享显存 2GB；Metal 3 |
| SSD | 三星 MZVLB512HAJQ-000L7，512.11GB，NVMe，PCIe 3.0 ×4；TRIM 开启 |
| 网卡 | Intel I226-V；系统枚举两个以太网接口。Intel AX210 Wi-Fi，Intel USB 蓝牙 8087:0032 |
| 显示/音频 | Mi Monitor，3840×2160 / 60Hz，HiDPI 1920×1080；当前仅枚举 HDMI 音频 |
| 系统/引导 | macOS 26.7.2（25G332）/ Darwin 25；OpenCore 1.0.9 DEBUG；SMBIOS MacPro7,1 |

主机品牌、主板商品型号与 BIOS 版本尚未可靠核实；MacPro7,1 是伪装机型，系统显示的 Intel Core i5 也不是真实处理器。详细字段、核验方式及原厂规格来源见 [硬件参数](docs/硬件参数.md)。

## 从这里开始

1. 阅读 [安装适配与恢复](docs/安装适配与恢复.md)，备份自己的 EFI，准备独立救援 U 盘。
2. 修改 `EFI/OC/config.plist` 的序列号、MLB、SystemUUID、ROM；当前公开值为空或全零，不能照搬用于 Apple 服务。
3. 核对物理核心数补丁、ACPI 路径、MMIO 白名单、网卡和目标 macOS 版本；再用匹配 `ocvalidate` 校验，并从 U 盘测试。

这是启动文件，不安装后台程序；停止使用时从 BIOS 选择原启动入口或恢复自己的 EFI 备份。不要删除 Windows 分区或覆盖 `EFI/Microsoft`。本仓库不含 Windows 引导、个人备份、NVRAM 转储或旧配置。

## 改了什么、驱动怎么选

- [配置改动](docs/配置改动.md)：原始 U 盘 EFI → 本机当前 EFI 的逐项变化；另列公开副本的脱敏差异。
- [驱动清单](docs/驱动清单.md)：实际版本、原机启用状态、公开包内容、用途和上游来源。
- [AMD 内核补丁](docs/AMD内核补丁.md)：27 项补丁明细，24 项启用，4 个物理核心的参数位置。
- [兼容状态与日志](docs/兼容状态与日志.md)：已观察、未验收和仍需排查的问题。
- [脱敏与许可](docs/脱敏与许可.md)：删除了哪些身份与文件，以及 GPLv3 和第三方组件的边界。

图形加速、4K 60Hz 和 CPU 传感器已有实际使用观察；USB 仍为通用映射，模拟音频/麦克风、睡眠及长时间网络稳定性尚未全部验收。CPU 包功耗不等于整机功耗。

关键文件为 `EFI/OC/config.plist`、`EFI/OC/Kexts/`、`EFI/OC/ACPI/` 和 `EFI-SHA256.json`。真正的本机主数据、原始 EFI、安装收据和备份只保留在维护现场，不在 GitHub；本仓库不能恢复你的磁盘数据或机器身份。自编配置整理、文档和工具采用 [GPL-3.0](LICENSE)，第三方组件保持各自原有许可。
