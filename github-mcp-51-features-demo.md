# GitHub MCP服务器51项功能完整演示

## 远程MCP配置
已配置使用远程GitHub MCP服务器：
- URL: `https://api.githubcopilot.com/mcp/`
- 认证: GitHub个人访问令牌
- 类型: HTTP远程服务器

## 51项功能分类演示

### 🔍 1. 上下文功能 (1项)
#### get_me - 获取当前用户信息
```json
{
  "tool": "get_me",
  "parameters": {},
  "description": "获取当前认证用户的GitHub个人资料信息"
}
```

### 🏗️ 2. 仓库管理功能 (15项)

#### 2.1 仓库操作
- **create_repository** - 创建新仓库
```json
{
  "tool": "create_repository",
  "parameters": {
    "name": "mcp-demo-2024",
    "description": "GitHub MCP服务器功能演示仓库",
    "private": false,
    "autoInit": true
  }
}
```

- **search_repositories** - 搜索仓库
```json
{
  "tool": "search_repositories",
  "parameters": {
    "query": "mcp server language:go stars:>100",
    "perPage": 10
  }
}
```

- **fork_repository** - 分叉仓库
```json
{
  "tool": "fork_repository",
  "parameters": {
    "owner": "microsoft",
    "repo": "vscode"
  }
}
```

#### 2.2 文件操作
- **get_file_contents** - 获取文件内容
```json
{
  "tool": "get_file_contents",
  "parameters": {
    "owner": "microsoft",
    "repo": "vscode",
    "path": "README.md"
  }
}
```

- **create_or_update_file** - 创建或更新文件
```json
{
  "tool": "create_or_update_file",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "path": "src/main.js",
    "content": "console.log('Hello from MCP!');",
    "message": "添加主程序文件",
    "branch": "main"
  }
}
```

- **delete_file** - 删除文件
```json
{
  "tool": "delete_file",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "path": "old-file.txt",
    "message": "删除旧文件",
    "branch": "main"
  }
}
```

- **push_files** - 推送多个文件
```json
{
  "tool": "push_files",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "branch": "main",
    "message": "批量添加演示文件",
    "files": [
      {
        "path": "docs/api.md",
        "content": "# API文档"
      },
      {
        "path": "tests/test.js",
        "content": "const assert = require('assert');"
      }
    ]
  }
}
```

#### 2.3 分支和标签
- **create_branch** - 创建分支
```json
{
  "tool": "create_branch",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "branch": "feature/mcp-integration",
    "from_branch": "main"
  }
}
```

- **list_branches** - 列出分支
```json
{
  "tool": "list_branches",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "perPage": 30
  }
}
```

- **get_commit** - 获取提交详情
```json
{
  "tool": "get_commit",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "sha": "abc123def456"
  }
}
```

- **list_commits** - 列出提交
```json
{
  "tool": "list_commits",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "perPage": 10
  }
}
```

- **get_tag** - 获取标签详情
```json
{
  "tool": "get_tag",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "tag": "v1.0.0"
  }
}
```

- **list_tags** - 列出标签
```json
{
  "tool": "list_tags",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "perPage": 20
  }
}
```

#### 2.4 代码搜索
- **search_code** - 搜索代码
```json
{
  "tool": "search_code",
  "parameters": {
    "query": "function MCP filename:*.js",
    "perPage": 50
  }
}
```

### 🐛 3. 问题管理功能 (12项)

#### 3.1 基本操作
- **create_issue** - 创建问题
```json
{
  "tool": "create_issue",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "title": "MCP服务器集成问题",
    "body": "## 问题描述\n需要集成GitHub MCP服务器的所有功能。\n\n## 任务清单\n- [ ] 测试所有51项功能\n- [ ] 创建演示文档\n- [ ] 验证远程MCP连接",
    "labels": ["enhancement", "mcp", "demo"]
  }
}
```

- **list_issues** - 列出问题
```json
{
  "tool": "list_issues",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "state": "open",
    "labels": ["mcp"],
    "perPage": 10
  }
}
```

- **get_issue** - 获取问题详情
```json
{
  "tool": "get_issue",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "issue_number": 1
  }
}
```

- **update_issue** - 更新问题
```json
{
  "tool": "update_issue",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "issue_number": 1,
    "title": "MCP服务器集成问题 [已更新]",
    "body": "问题已更新，包含更多详细信息。",
    "labels": ["enhancement", "mcp", "demo", "in-progress"]
  }
}
```

- **add_issue_comment** - 添加问题评论
```json
{
  "tool": "add_issue_comment",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "issue_number": 1,
    "body": "进展更新：已完成30/51项功能的测试。"
  }
}
```

- **search_issues** - 搜索问题
```json
{
  "tool": "search_issues",
  "parameters": {
    "query": "repo:your-username/mcp-demo-2024 is:issue label:mcp",
    "perPage": 20
  }
}
```

#### 3.2 子问题管理
- **add_sub_issue** - 添加子问题
```json
{
  "tool": "add_sub_issue",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "issue_number": 1,
    "sub_issue_id": 2
  }
}
```

- **list_sub_issues** - 列出子问题
```json
{
  "tool": "list_sub_issues",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "issue_number": 1
  }
}
```

- **remove_sub_issue** - 移除子问题
```json
{
  "tool": "remove_sub_issue",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "issue_number": 1,
    "sub_issue_id": 2
  }
}
```

- **reprioritize_sub_issue** - 重新排序子问题
```json
{
  "tool": "reprioritize_sub_issue",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "issue_number": 1,
    "sub_issue_id": 3,
    "after_id": 2
  }
}
```

- **assign_copilot_to_issue** - 分配Copilot处理问题
```json
{
  "tool": "assign_copilot_to_issue",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "issueNumber": 1
  }
}
```

### 🔄 4. 拉取请求功能 (15项)

#### 4.1 基本操作
- **create_pull_request** - 创建拉取请求
```json
{
  "tool": "create_pull_request",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "title": "添加完整的MCP功能演示",
    "head": "feature/mcp-demo",
    "base": "main",
    "body": "## 变更概述\n这个PR添加了GitHub MCP服务器所有51项功能的完整演示。\n\n## 新增内容\n- 完整的API调用示例\n- 使用文档\n- 测试脚本\n\n## 测试\n- [x] 所有功能已验证\n- [x] 文档已更新\n- [x] 示例代码可运行",
    "draft": false
  }
}
```

- **list_pull_requests** - 列出拉取请求
```json
{
  "tool": "list_pull_requests",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "state": "open",
    "perPage": 10
  }
}
```

- **get_pull_request** - 获取拉取请求详情
```json
{
  "tool": "get_pull_request",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1
  }
}
```

- **update_pull_request** - 更新拉取请求
```json
{
  "tool": "update_pull_request",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1,
    "title": "添加完整的MCP功能演示 [已更新]",
    "body": "PR已更新，包含更多示例和文档。"
  }
}
```

- **merge_pull_request** - 合并拉取请求
```json
{
  "tool": "merge_pull_request",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1,
    "merge_method": "squash",
    "commit_title": "添加完整的MCP功能演示",
    "commit_message": "包含所有51项功能的演示和使用示例"
  }
}
```

#### 4.2 PR详情和文件
- **get_pull_request_files** - 获取拉取请求文件
```json
{
  "tool": "get_pull_request_files",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1
  }
}
```

- **get_pull_request_diff** - 获取拉取请求差异
```json
{
  "tool": "get_pull_request_diff",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1
  }
}
```

- **get_pull_request_reviews** - 获取拉取请求审查
```json
{
  "tool": "get_pull_request_reviews",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1
  }
}
```

- **get_pull_request_status** - 获取拉取请求状态
```json
{
  "tool": "get_pull_request_status",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1
  }
}
```

- **search_pull_requests** - 搜索拉取请求
```json
{
  "tool": "search_pull_requests",
  "parameters": {
    "query": "repo:your-username/mcp-demo-2024 is:pr label:mcp",
    "perPage": 20
  }
}
```

#### 4.3 PR审查流程
- **create_pending_pull_request_review** - 创建待处理审查
```json
{
  "tool": "create_pending_pull_request_review",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1
  }
}
```

- **add_comment_to_pending_review** - 添加审查评论
```json
{
  "tool": "add_comment_to_pending_review",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1,
    "path": "README.md",
    "body": "建议在文档中添加更多使用示例。",
    "line": 10,
    "subjectType": "LINE"
  }
}
```

- **submit_pending_pull_request_review** - 提交审查
```json
{
  "tool": "submit_pending_pull_request_review",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1,
    "event": "APPROVE",
    "body": "代码质量良好，文档完整，可以合并。"
  }
}
```

- **delete_pending_pull_request_review** - 删除待处理审查
```json
{
  "tool": "delete_pending_pull_request_review",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1
  }
}
```

- **update_pull_request_branch** - 更新拉取请求分支
```json
{
  "tool": "update_pull_request_branch",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "pullNumber": 1
  }
}
```

### ⚙️ 5. GitHub Actions功能 (11项)

#### 5.1 工作流管理
- **list_workflows** - 列出工作流
```json
{
  "tool": "list_workflows",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "perPage": 10
  }
}
```

- **list_workflow_runs** - 列出工作流运行
```json
{
  "tool": "list_workflow_runs",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "workflow_id": "ci.yml",
    "perPage": 5
  }
}
```

- **get_workflow_run** - 获取工作流运行详情
```json
{
  "tool": "get_workflow_run",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "run_id": 123456789
  }
}
```

- **run_workflow** - 运行工作流
```json
{
  "tool": "run_workflow",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "workflow_id": "demo.yml",
    "ref": "main",
    "inputs": {
      "environment": "staging",
      "verbose": true
    }
  }
}
```

#### 5.2 工作流控制
- **cancel_workflow_run** - 取消工作流运行
```json
{
  "tool": "cancel_workflow_run",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "run_id": 123456789
  }
}
```

- **rerun_workflow_run** - 重新运行工作流
```json
{
  "tool": "rerun_workflow_run",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "run_id": 123456789
  }
}
```

- **rerun_failed_jobs** - 重新运行失败的任务
```json
{
  "tool": "rerun_failed_jobs",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "run_id": 123456789
  }
}
```

#### 5.3 工作流详情
- **list_workflow_jobs** - 列出工作流任务
```json
{
  "tool": "list_workflow_jobs",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "run_id": 123456789
  }
}
```

- **get_job_logs** - 获取任务日志
```json
{
  "tool": "get_job_logs",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "job_id": 987654321,
    "return_content": true,
    "tail_lines": 100
  }
}
```

- **get_workflow_run_logs** - 获取工作流运行日志
```json
{
  "tool": "get_workflow_run_logs",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "run_id": 123456789
  }
}
```

- **delete_workflow_run_logs** - 删除工作流运行日志
```json
{
  "tool": "delete_workflow_run_logs",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "run_id": 123456789
  }
}
```

- **list_workflow_run_artifacts** - 列出工作流运行构件
```json
{
  "tool": "list_workflow_run_artifacts",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "run_id": 123456789
  }
}
```

- **download_workflow_run_artifact** - 下载工作流运行构件
```json
{
  "tool": "download_workflow_run_artifact",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "artifact_id": 555666777
  }
}
```

- **get_workflow_run_usage** - 获取工作流使用统计
```json
{
  "tool": "get_workflow_run_usage",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "run_id": 123456789
  }
}
```

### 🔒 6. 安全功能 (6项)

#### 6.1 代码扫描
- **list_code_scanning_alerts** - 列出代码扫描警报
```json
{
  "tool": "list_code_scanning_alerts",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "state": "open",
    "severity": "high"
  }
}
```

- **get_code_scanning_alert** - 获取代码扫描警报详情
```json
{
  "tool": "get_code_scanning_alert",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "alertNumber": 1
  }
}
```

#### 6.2 依赖扫描
- **list_dependabot_alerts** - 列出Dependabot警报
```json
{
  "tool": "list_dependabot_alerts",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "state": "open",
    "severity": "critical"
  }
}
```

- **get_dependabot_alert** - 获取Dependabot警报详情
```json
{
  "tool": "get_dependabot_alert",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "alertNumber": 1
  }
}
```

#### 6.3 密钥扫描
- **list_secret_scanning_alerts** - 列出密钥扫描警报
```json
{
  "tool": "list_secret_scanning_alerts",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "state": "open"
  }
}
```

- **get_secret_scanning_alert** - 获取密钥扫描警报详情
```json
{
  "tool": "get_secret_scanning_alert",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "alertNumber": 1
  }
}
```

### 💬 7. 讨论功能 (4项)

- **list_discussions** - 列出讨论
```json
{
  "tool": "list_discussions",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "perPage": 10
  }
}
```

- **get_discussion** - 获取讨论详情
```json
{
  "tool": "get_discussion",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "discussionNumber": 1
  }
}
```

- **get_discussion_comments** - 获取讨论评论
```json
{
  "tool": "get_discussion_comments",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "discussionNumber": 1,
    "perPage": 20
  }
}
```

- **list_discussion_categories** - 列出讨论分类
```json
{
  "tool": "list_discussion_categories",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024"
  }
}
```

### 🔔 8. 通知功能 (6项)

- **list_notifications** - 列出通知
```json
{
  "tool": "list_notifications",
  "parameters": {
    "filter": "default",
    "perPage": 20
  }
}
```

- **get_notification_details** - 获取通知详情
```json
{
  "tool": "get_notification_details",
  "parameters": {
    "notificationID": "123456"
  }
}
```

- **mark_all_notifications_read** - 标记所有通知为已读
```json
{
  "tool": "mark_all_notifications_read",
  "parameters": {}
}
```

- **dismiss_notification** - 忽略通知
```json
{
  "tool": "dismiss_notification",
  "parameters": {
    "threadID": "123456",
    "state": "done"
  }
}
```

- **manage_notification_subscription** - 管理通知订阅
```json
{
  "tool": "manage_notification_subscription",
  "parameters": {
    "notificationID": "123456",
    "action": "watch"
  }
}
```

- **manage_repository_notification_subscription** - 管理仓库通知订阅
```json
{
  "tool": "manage_repository_notification_subscription",
  "parameters": {
    "owner": "your-username",
    "repo": "mcp-demo-2024",
    "action": "watch"
  }
}
```

### 👥 9. 组织和用户功能 (2项)

- **search_orgs** - 搜索组织
```json
{
  "tool": "search_orgs",
  "parameters": {
    "query": "mcp type:org",
    "perPage": 10
  }
}
```

- **search_users** - 搜索用户
```json
{
  "tool": "search_users",
  "parameters": {
    "query": "location:China followers:>1000",
    "perPage": 10
  }
}
```

## 项目更新演示

### 更新流程示例
1. **创建功能分支**
2. **添加新功能**
3. **创建拉取请求**
4. **代码审查**
5. **合并更新**

### 实际更新操作
```bash
# 1. 创建功能分支
create_branch({
  "owner": "your-username",
  "repo": "mcp-demo-2024",
  "branch": "feature/update-documentation",
  "from_branch": "main"
})

# 2. 更新文件
create_or_update_file({
  "owner": "your-username",
  "repo": "mcp-demo-2024",
  "path": "CHANGELOG.md",
  "content": "## [1.1.0] - 2024-07-27\n### Added\n- 完整的51项MCP功能演示\n- 远程MCP配置示例\n- 项目更新和回滚指南",
  "message": "更新变更日志",
  "branch": "feature/update-documentation"
})

# 3. 创建PR
create_pull_request({
  "owner": "your-username",
  "repo": "mcp-demo-2024",
  "title": "更新文档和添加新功能演示",
  "head": "feature/update-documentation",
  "base": "main",
  "body": "这个PR更新了项目文档并添加了新的功能演示。"
})
```

## 项目回滚演示

### 回滚策略
1. **使用Git回滚**
2. **使用GitHub Releases**
3. **使用标签回滚**

### 实际回滚操作
```bash
# 1. 查看提交历史
list_commits({
  "owner": "your-username",
  "repo": "mcp-demo-2024",
  "perPage": 5
})

# 2. 回滚特定文件到之前版本
create_or_update_file({
  "owner": "your-username",
  "repo": "mcp-demo-2024",
  "path": "src/main.js",
  "content": "// 回滚到稳定版本的代码",
  "message": "回滚main.js到稳定版本",
  "branch": "main"
})

# 3. 创建回滚标签
create_or_update_file({
  "owner": "your-username",
  "repo": "mcp-demo-2024",
  "path": ".github/workflows/rollback.yml",
  "content": "name: Rollback Workflow\non:\n  workflow_dispatch:\n    inputs:\n      commit_sha:\n        description: 'Commit SHA to rollback to'\n        required: true",
  "message": "添加回滚工作流"
})
```

## 使用总结

### 功能统计
- ✅ 总功能数：51项
- ✅ 已配置：远程MCP
- ✅ 认证方式：GitHub个人访问令牌
- ✅ 连接方式：HTTP API

### 最佳实践
1. **使用环境变量存储令牌**
2. **限制令牌权限范围**
3. **定期轮换令牌**
4. **使用分支保护规则**
5. **配置自动化测试**

### 故障排除
- **401错误**：检查令牌权限
- **403错误**：验证组织策略
- **404错误**：确认资源存在
- **速率限制**：使用分页参数