<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%23%201%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/wchao-hermes/hermes-howto?style=flat&color=gold)](https://github.com/wchao-hermes/hermes-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wchao-hermes/hermes-howto?style=flat)](https://github.com/wchao-hermes/hermes-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)](CHANGELOG.md)
[![Hermes Agent](https://img.shields.io/badge/Hermes_Agent-Tương_thích-purple)](https://hermes-agent.dev)

🌐 **Ngôn ngữ / Language / 语言 / Мова:** [English](../README.md) | [Tiếng Việt](README.md) | [中文](zh/README.md) | [Українська](../uk/README.md)

# Làm Chủ Hermes Agent Trong Một Cuối Tuần

Từ chat cơ bản đến điều phối agents, skills, MCP servers, voice, và tích hợp nhắn tin — với hướng dẫn trực quan, template có thể sao chép-dán, và lộ trình học tập có cấu trúc.

**[Bắt Đầu Trong 15 Phút](#bắt-đầu-trong-15-phút)** | **[Tìm Cấp Độ Của Bạn](#không-chắc-bắt-đầu-từ-đâu)** | **[Duyệt Danh Mục Tính Năng](../INDEX.md)**

---

## Mục Lục

- [Vấn Đề](#vấn-đề)
- [Hermes How To Giải Quyết Điều Này Như Thế Nào](#hermes-how-to-giải-quyết-điều-này-như-thế-nào)
- [Cách Hoạt Động](#cách-hoạt-động)
- [Không Chắc Bắt Đầu Từ Đâu?](#không-chắc-bắt-đầu-từ-đâu)
- [Bắt Đầu Trong 15 Phút](#bắt-đầu-trong-15-phút)
- [Bạn Có Thể Xây Dựng Gì Với Điều Này?](#bạn-có-thể-xây-dựng-gì-với-điều-này)
- [FAQ](#faq)
- [Đóng Góp](#đóng-góp)
- [Giấy Phép](#giấy-phép)

---

## Vấn Đề

Bạn đã cài đặt Hermes Agent. Bạn đã chạy vài prompts. Bây giờ sao?

- **Tài liệu chính thức mô tả các tính năng — nhưng không hướng dẫn cách kết hợp chúng.** Bạn biết skills tồn tại, nhưng không biết cách chuỗi chúng với delegation, voice, và MCP thành workflow thực sự tiết kiệm thời gian.
- **Không có lộ trình học tập rõ ràng.** Bạn nên học MCP trước hay delegation? Memory trước hay personality? Bạn kết thúc bằng việc đọc lướt mọi thứ và không làm chủ được gì.
- **Ví dụ quá cơ bản.** Một skill "hello world" không giúp bạn xây dựng một hệ thống chăm sóc khách hàng sản xuất sử dụng messaging gateway, voice, và các tác vụ được lên lịch.

Bạn đang để 90% sức mạnh của Hermes Agent trên bàn — và bạn không biết những gì bạn không biết.

---

## Hermes How To Giải Quyết Điều Này Như Thế Nào

Đây không phải là một tài liệu tham khảo tính năng khác. Đây là **hướng dẫn có cấu trúc, trực quan, dựa trên ví dụ** dạy bạn sử dụng mọi tính năng của Hermes Agent với các template thực tế bạn có thể sao chép vào dự án ngay hôm nay.

| | Tài Liệu Chính Thức | Hướng Dẫn Này |
|--|---------------------|---------------|
| **Định dạng** | Tài liệu tham khảo | Hướng dẫn trực quan với biểu đồ Mermaid |
| **Chiều sâu** | Mô tả tính năng | Cách hoạt động bên trong |
| **Ví dụ** | Đoạn code cơ bản | Template sẵn sàng sản xuất |
| **Cấu trúc** | Theo tính năng | Lộ trình học tập từ cơ bản đến nâng cao |
| **Onboarding** | Tự hướng dẫn | Lộ trình có thời gian ước tính |
| **Tự Đánh Giá** | Không có | Bài kiểm tra tìm lỗ hổng |

### Bạn nhận được:

- **14 modules hướng dẫn** bao gồm mọi tính năng của Hermes Agent — từ quickstart đến context references
- **Copy-paste configs** — skills, delegation templates, MCP configs, voice settings, messaging gateway integrations, và plugin bundles
- **Biểu đồ Mermaid** hiển thị cách mỗi tính năng hoạt động bên trong, để bạn hiểu *tại sao*, không chỉ *như thế nào*
- **Lộ trình học tập có hướng dẫn** đưa bạn từ người mới bắt đầu đến người dùng nâng cao trong 11-13 giờ
- **Tự đánh giá tích hợp** — chạy quiz sau mỗi module để tìm lỗ hổng

**[Bắt Đầu Lộ Trình Học Tập](../LEARNING-ROADMAP.md)**

---

## Cách Hoạt Động

### 1. Tìm cấp độ của bạn

Làm bài kiểm tra tự đánh giá hoặc chọn cấp độ kinh nghiệm hiện tại của bạn. Nhận lộ trình cá nhân hóa dựa trên những gì bạn đã biết.

### 2. Theo lộ trình được hướng dẫn

Làm việc qua 14 modules theo thứ tự — mỗi module xây dựng trên module trước. Sao chép template trực tiếp vào dự án của bạn khi học.

### 3. Kết hợp các tính năng thành workflows

Sức mạnh thực sự nằm ở việc kết hợp các tính năng. Học cách kết nối skills + delegation + MCP + voice + messaging gateway + cron thành các pipeline tự động xử lý chăm sóc khách hàng, giám sát, và tích hợp.

### 4. Kiểm tra sự hiểu biết của bạn

Chạy quiz sau mỗi module. Quiz chỉ ra những gì bạn còn thiếu để bạn có thể lấp đầy nhanh chóng.

---

## Không Chắc Bắt Đầu Từ Đâu?

Làm bài kiểm tra tự đánh giá hoặc chọn cấp độ của bạn:

| Cấp Độ | Bạn có thể... | Bắt đầu tại | Thời gian |
|--------|---------------|-------------|-----------|
| **Người mới** | Khởi động Hermes Agent và chat | [Quickstart](../01-quickstart/) | ~2.5 giờ |
| **Trung cấp** | Sử dụng Memory và Skills | [Skills](../03-skills/) | ~3.5 giờ |
| **Nâng cao** | Cấu hình MCP và Delegation | [Delegation](../04-delegation/) | ~5 giờ |

**Lộ trình học tập đầy đủ với 14 modules:**

| Thứ tự | Module | Cấp độ | Thời gian |
|--------|--------|--------|----------|
| 1 | [Quickstart](../01-quickstart/) | Người mới | 30 phút |
| 2 | [Memory](../02-memory/) | Người mới+ | 45 phút |
| 3 | [Skills](../03-skills/) | Trung cấp | 1 giờ |
| 4 | [Delegation](../04-delegation/) | Trung cấp+ | 1.5 giờ |
| 5 | [MCP](../05-mcp/) | Trung cấp+ | 1 giờ |
| 6 | [Voice](../06-voice/) | Trung cấp | 1 giờ |
| 7 | [Messaging Gateway](../07-messaging-gateway/) | Nâng cao | 1.5 giờ |
| 8 | [Cron](../08-cron/) | Trung cấp | 45 phút |
| 9 | [SOUL/Personality](../09-soul-personality/) | Trung cấp | 1 giờ |
| 10 | [Toolsets](../10-toolsets/) | Nâng cao | 1.5 giờ |
| 11 | [Plugins](../11-plugins/) | Nâng cao | 2 giờ |
| 12 | [Checkpoints](../12-checkpoints/) | Trung cấp | 45 phút |
| 13 | [Providers](../13-providers/) | Trung cấp | 1 giờ |
| 14 | [Context Refs](../14-context-refs/) | Nâng cao | 1 giờ |

**[Lộ Trình Học Tập Đầy Đủ](../LEARNING-ROADMAP.md)**

---

## Bắt Đầu Trong 15 Phút

```bash
# 1. Clone hướng dẫn này
git clone https://github.com/wchao-hermes/hermes-howto.git
cd hermes-howto

# 2. Copy skill đầu tiên của bạn
mkdir -p ~/.hermes/skills
cp -r 03-skills/example-skill ~/.hermes/skills/

# 3. Thử nó — tương tác với skill trong Hermes Agent

# 4. Sẵn sàng cho nhiều hơn? Thiết lập project memory:
cp 02-memory/project-HERMES.md /đường/dẫn/dự án/HERMES.md

# 5. Cấu hình provider:
cp 13-providers/provider-examples/standard-providers.yaml ~/.hermes/providers/
```

Muốn cài đặt đầy đủ? Đây là **cài đặt thiết yếu trong 1 giờ**:

```bash
# Skills (15 phút)
cp -r 03-skills/* ~/.hermes/skills/

# Project memory (15 phút)
cp 02-memory/project-HERMES.md ./HERMES.md

# Delegation templates (15 phút)
cp -r 04-delegation/* ~/.hermes/delegation/

# MCP servers (15 phút)
export GITHUB_TOKEN="***"
hermes mcp add github -- npx -y @modelcontextprotocol/server-github

# Mục tiêu cuối tuần: thêm voice, messaging gateway, cron, plugins
# Theo lộ trình học tập để được hướng dẫn cài đặt
```

---

## Bạn Có Thể Xây Dựng Gì Với Điều Này?

| Use Case | Tính Năng Bạn Sẽ Kết Hợp |
|----------|--------------------------|
| **Bot Chăm Sóc Khách Hàng** | Messaging Gateway + Voice + Skills + MCP |
| **Giám Sát Theo Lịch** | Cron + Delegation + Checkpoints + Providers |
| **Multi-agent Pipeline** | Delegation + SOUL/Personality + Toolsets + Plugins |
| **Trợ Lý Giọng Nói** | Voice + Memory + Skills + MCP |
| **Onboarding Team** | Memory + Plugins + Context Refs |
| **DevOps Automation** | Cron + MCP + Checkpoints + Providers |
| **Refactoring Phức Tạp** | Checkpoints + Planning + Delegation |

---

## FAQ

**Điều này có miễn phí không?**
Có. MIT licensed, miễn phí mãi mãi. Sử dụng trong dự án cá nhân, tại công ty, trong team của bạn — không có hạn chế ngoài việc giữ lại thông báo giấy phép.

**Điều này có được duy trì không?**
Tích cực. Hướng dẫn được đồng bộ với mọi phiên bản phát hành của Hermes Agent.

**Điều này khác gì so với tài liệu chính thức?**
Tài liệu chính thức là tài liệu tham khảo tính năng. Hướng dẫn này là một tutorial với biểu đồ, template sẵn sàng sản xuất, và lộ trình học tập tiến bộ. Chúng bổ sung cho nhau — bắt đầu ở đây để học, tham khảo tài liệu khi bạn cần chi tiết.

**Mất bao lâu để hoàn thành mọi thứ?**
11-13 giờ cho lộ trình đầy đủ. Nhưng bạn sẽ có giá trị ngay lập tức trong 15 phút — chỉ cần copy một skill template và thử nó.

**Tôi có thể đóng góp không?**
Tuyệt đối. Xem [CONTRIBUTING.md](../CONTRIBUTING.md) để biết hướng dẫn. Chúng tôi chào đón ví dụ mới, sửa lỗi, cải thiện tài liệu, và template cộng đồng.

---

## Bắt Đầu Làm Chủ Hermes Agent Hôm Nay

Bạn đã cài đặt Hermes Agent rồi. Thứ duy nhất giữa bạn và năng suất 10x là biết cách sử dụng nó. Hướng dẫn này cung cấp cho bạn lộ trình có cấu trúc, giải thích trực quan, và template copy-paste để đến đó.

MIT licensed. Miễn phí mãi mãi. Clone nó, fork nó, biến nó thành của bạn.

**[Bắt Đầu Lộ Trình Học Tập](../LEARNING-ROADMAP.md)** | **[Duyệt Danh Mục Tính Năng](../INDEX.md)** | **[Bắt Đầu Trong 15 Phút](#bắt-đầu-trong-15-phút)**

---

<details>
<summary>Điều Hướng Nhanh — Tất Cả Tính Năng</summary>

| Tính năng | Mô tả | Thư mục |
|-----------|-------|---------|
| **Danh Mục Tính Năng** | Tham khảo đầy đủ với lệnh cài đặt | [INDEX.md](../INDEX.md) |
| **Quickstart** | Hướng dẫn bắt đầu | [01-quickstart/](../01-quickstart/) |
| **Memory** | Context liên tục | [02-memory/](../02-memory/) |
| **Skills** | Khả năng có thể tái sử dụng | [03-skills/](../03-skills/) |
| **Delegation** | Ủy thác tác vụ | [04-delegation/](../04-delegation/) |
| **MCP Protocol** | Truy cập công cụ bên ngoài | [05-mcp/](../05-mcp/) |
| **Voice** | Tương tác giọng nói | [06-voice/](../06-voice/) |
| **Messaging Gateway** | Tích hợp nền tảng nhắn tin | [07-messaging-gateway/](../07-messaging-gateway/) |
| **Cron** | Tác vụ được lên lịch | [08-cron/](../08-cron/) |
| **SOUL/Personality** | Cấu hình personality agent | [09-soul-personality/](../09-soul-personality/) |
| **Toolsets** | Bộ sưu tập công cụ | [10-toolsets/](../10-toolsets/) |
| **Plugins** | Tính năng bundled | [11-plugins/](../11-plugins/) |
| **Checkpoints** | Ảnh chụp & tua session | [12-checkpoints/](../12-checkpoints/) |
| **Providers** | Cấu hình AI provider | [13-providers/](../13-providers/) |
| **Context Refs** | Tham chiếu context | [14-context-refs/](../14-context-refs/) |

</details>

<details>
<summary>So Sánh Tính Năng</summary>

| Tính năng | Kích hoạt | Persistence | Tốt nhất cho |
|-----------|-----------|-------------|--------------|
| **Skills** | Auto-invoked | Filesystem | Workflows tự động |
| **Delegation** | Auto-delegated | Isolated context | Phân phối tác vụ |
| **Memory** | Auto-loaded | Cross-session | Học tập dài hạn |
| **MCP Protocol** | Auto-queried | Real-time | Truy cập dữ liệu trực tiếp |
| **Voice** | User-initiated | Session | Tương tác rảnh tay |
| **Messaging Gateway** | Event-triggered | Real-time | Tích hợp nền tảng |
| **Cron** | Scheduled | Persistent | Tác vụ định kỳ |
| **SOUL/Personality** | Configured | Persistent | Hành vi tùy chỉnh |
| **Toolsets** | Auto-available | Session | Khả năng mở rộng |
| **Plugins** | One command | All features | Giải pháp hoàn chỉnh |
| **Checkpoints** | Manual/Auto | Session-based | Thử nghiệm an toàn |
| **Providers** | Configured | Persistent | Lựa chọn AI backend |
| **Context Refs** | Auto-injected | Per-request | Context động |

</details>
