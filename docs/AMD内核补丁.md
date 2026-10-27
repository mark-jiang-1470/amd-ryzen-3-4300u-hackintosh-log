# AMD 内核补丁明细

从当前实际 EFI 导出；不是新建或升级补丁。共 27 项，24 项启用；包含不同 Darwin 版本的互斥范围，Enabled=true 不等于在当前系统全部命中。四处核心数常量为 4 个物理核心。

| 索引 | 启用 | 说明 | MinKernel | MaxKernel | Replace（hex） |
|---|---|---|---|---|---|
| 0 | 是 | algrey ／ Force cpuid_cores_per_package to constant (user-specified) ／ 10.13-10.14 | 17.0.0 | 18.99.99 | b80400000000 |
| 1 | 是 | algrey ／ Force cpuid_cores_per_package to constant (user-specified) ／ 10.15-11.0 | 19.0.0 | 20.99.99 | ba0400000000 |
| 2 | 是 | algrey ／ Force cpuid_cores_per_package to constant (user-specified) ／ 12.0-13.2 | 21.0.0 | 22.3.99 | ba0400000090 |
| 3 | 是 | algrey ／ Force cpuid_cores_per_package to constant (user-specified) ／ 13.3+ | 22.4.0 | 25.99.99 | ba04000000 |
| 4 | 是 | algrey ／ _commpage_populate ／ Remove rdmsr ／ 10.13+ | 17.0.0 | 25.99.99 | 66906690669090 |
| 5 | 是 | algrey ／ _cpuid_set_cache_info ／ Set CPUID proper instead of 4 ／ 10.13+ | 17.0.0 | 25.99.99 | b81d0000804489f14489 |
| 6 | 是 | algrey ／ _cpuid_set_generic_info ／ Remove wrmsr(0x8B) ／ 10.13+ | 17.0.0 | 25.99.99 | 6690669066906690669090 |
| 7 | 是 | algrey ／ _cpuid_set_generic_info ／ Replace rdmsr(0x8B) with constant 186 ／ 10.13+ | 17.0.0 | 25.99.99 | baba0000006690 |
| 8 | 是 | algrey ／ _cpuid_set_generic_info ／ Set flag=1 ／ 10.13+ | 17.0.0 | 25.99.99 | b201660f1f8400000000006690 |
| 9 | 是 | algrey ／ _cpuid_set_generic_info ／ Disable check to allow leaf7 ／ 10.13+ | 17.0.0 | 23.99.99 | 00000f82 |
| 10 | 是 | algrey ／ _cpuid_set_generic_info ／ Disable check to allow leaf7 ／ 15.0+ | 24.0.0 | 25.99.99 | 00000f82 |
| 11 | 是 | algrey ／ _cpuid_set_info ／ GenuineIntel to AuthenticAMD ／ 10.13-11.0 | 17.0.0 | 20.99.99 | 41757468656e746963414d4400 |
| 12 | 是 | Goldfish64, algrey ／ Bypass GenuineIntel check panic ／ 12.0+ | 21.0.0 | 25.99.99 | 90909090909031d2b301 |
| 13 | 是 | algrey ／ _cpuid_set_cpufamily ／ Force CPUFAMILY_INTEL_PENRYN ／ 10.13-11.2 | 17.0.0 | 20.3.0 | bbbc4fea78e95d00000090 |
| 14 | 是 | algrey ／ _cpuid_set_cpufamily ／ Force CPUFAMILY_INTEL_PENRYN ／ 11.3+ | 20.4.0 | 25.99.99 | babc4fea7831dbeb |
| 15 | 是 | algrey ／ _i386_init ／ Remove 3 rdmsr calls ／ 10.13+ | 17.0.0 | 25.99.99 | 660f1f840000000000660f1f840000000000660f1f840000000000660f1f840000000000660f1f440000 |
| 16 | 是 | algrey, XLNC ／ Remove version check and panic ／ 10.13+ | 17.0.0 | 25.99.99 | 25fc0000000f1f00 |
| 17 | 是 | CaseySJ ／ probeBusGated ／ Disable 10 bit tags ／ 12.0-15.x | 21.0.0 | 24.99.99 | 00000300 |
| 18 | 是 | CaseySJ ／ probeBusGated ／ Disable 10 bit tags ／ 26.0+ | 25.0.0 | 25.99.99 | 00000200 |
| 19 | 否 | CaseySJ ／ IOPCIIsHotplugPort ／ Fix PCI bus enumeration on AM5 ／ 13.0+ | 22.0.0 | 25.99.99 | 0000eb00 |
| 20 | 是 | Visual ／ thread_quantum_expire, thread_unblock, thread_invoke ／ Remove non-monotonic time panic ／ 12.0+ | 21.0.0 | 25.99.99 | 0000000000000000000000000000669066906690 |
| 21 | 是 | Visual ／ thread_invoke, thread_dispatch ／ Remove non-monotonic time panic ／ 12.0-26.3 | 21.0.0 | 25.3.99 | 00000000000000669066906690 |
| 22 | 是 | laobamac ／ thread_invoke, thread_dispatch ／ Remove non-monotonic time panic ／ 26.4+ | 25.4.0 | 25.99.99 | 00000000000000669066906690 |
| 23 | 否 | algrey ／ _mtrr_update_action ／ fix PAT ／ 10.13+ | 17.0.0 | 23.99.99 | b977020000b806010700ba060107000f1f4000 |
| 24 | 是 | Shaneee ／ _mtrr_update_action ／ Fix PAT ／ 10.13+ | 17.0.0 | 23.99.99 | b977020000b806060606ba060606060f300f09 |
| 25 | 否 | Algrey / Zormeister ／ _mtrr_update_action ／ Fix PAT ／ 15.0+ | 24.0.0 | 25.99.99 | 89c0b806010700ba060107000f309090 |
| 26 | 是 | Shaneee / Zormeister ／ _mtrr_update_action ／ Fix PAT ／ 15.0+ | 24.0.0 | 25.99.99 | 89c0b806060606ba060606060f309090 |
