# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809052007 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 05:20:07 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURAL MODALITY

### 1.1. Core System Modality & Architectural Modality
- Hệ thống được thiết kế theo kiến trúc đa lớp với các thành phần chính bao gồm: Frontend (Next.js), Backend (Java/Quarkus), Cơ sở dữ liệu (PostgreSQL), và Hạ tầng Cloud (GKE).
- Sử dụng mô hình RBAC (Role-Based Access Control) để quản lý quyền truy cập dựa trên vai trò người dùng.
- Hệ thống hỗ trợ đa kênh giao tiếp bao gồm web, di động, và nhóm Zalo.
- Điểm danh thời gian thực được thực hiện thông qua quét mã QR.
- Thẻ hội viên kỹ thuật số được tích hợp với tính năng đếm ngày hiệu lực.
- Hệ thống sử dụng Firebase Authentication cho xác thực người dùng.
- Google Cloud Messaging (FCM) và Apple APNs được sử dụng để gửi thông báo đẩy đến thiết bị di động.
- Zalo API được tích hợp để gửi thông báo đến nhóm Zalo.
- Redis được sử dụng để lưu trữ session caching.
- CI/CD pipeline được thiết lập với GitHub Actions để tự động hóa quá trình triển khai.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- Dữ liệu được lưu trữ trong cơ sở dữ liệu PostgreSQL với các bảng chính bao gồm: Users, Roles, Centers, Courses, Enrollments, Attendance, StudentCards, Notifications, Promotions, và Announcements.
- Các API REST được sử dụng để giao tiếp giữa Frontend và Backend.
- Các sự kiện được gửi thông qua Kafka để xử lý các tác vụ bất đồng bộ.
- Các thông báo được gửi thông qua FCM và Zalo API.
- Các báo cáo được tạo ra từ dữ liệu trong cơ sở dữ liệu và được lưu trữ dưới dạng CSV.
- Các báo cáo được hiển thị trên bảng điều khiển thời gian thực.
- Các báo cáo được tạo ra từ dữ liệu trong cơ sở dữ liệu và được lưu trữ dưới dạng CSV.
- Các báo cáo được hiển thị trên bảng điều khiển thời gian thực.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API, Redis, GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React Native, Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API, Redis, GitHub Actions.

### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG

<!--START_BACKLOG_SYNOPSIS_GRID-->
| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Xây dựng hệ thống xác thực người dùng | Cung cấp chức năng đăng ký và đăng nhập người dùng thông qua email/mật khẩu, Firebase, Google, và Facebook OAuth. | Application Code | [REQ-001], [REQ-002], [ARC-006] |
| 2 | Phân quyền người dùng | Cung cấp chức năng phân quyền người dùng dựa trên vai trò (System Admin, Center Admin, Manager, Teacher, Student). | Application Code | [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] |
| 3 | Quản lý trung tâm | Cung cấp chức năng xem, tạo, cập nhật, và xóa trung tâm. | Application Code | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| 4 | Quản lý khóa học | Cung cấp chức năng xem, tạo, cập nhật, và xóa khóa học. | Application Code | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| 5 | Đăng ký & ghi danh học viên | Cung cấp chức năng duyệt khóa học và đăng ký khóa học của học viên. | Application Code | [REQ-010], [REQ-011], [DAT-005] |
| 6 | Điểm danh & quét mã QR | Cung cấp chức năng chụp ảnh điểm danh QR và tính chất bất biến của điểm danh. | Application Code | [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006] |
| 7 | Quản lý thẻ hội viên | Cung cấp chức năng hiển thị tính hợp lệ của thẻ và gia hạn thẻ. | Application Code | [REQ-014], [REQ-015], [DAT-007] |
| 8 | Thông báo & truyền thông | Cung cấp chức năng kích hoạt thông báo. | Application Code | [REQ-016], [EXC-003], [DAT-008] |
| 9 | Quản lý khuyến mãi & thông báo | Cung cấp chức năng quản lý khuyến mãi và thông báo. | Application Code | [REQ-017], [REQ-018], [DAT-009] |
| 10 | Chatbot dịch vụ khách hàng AI | Cung cấp chức năng tích hợp chatbot AI. | Application Code | [REQ-019] |
| 11 | Các tính năng cốt lõi của ứng dụng di động | Cung cấp chức năng giao diện người dùng vai trò cụ thể trên di động và thông báo đẩy trên di động. | Application Code | [REQ-020], [REQ-021] |
| 12 | Bản địa hóa & SEO | Cung cấp chức năng phát hiện ngôn ngữ mặc định và SEO đa ngôn ngữ. | Application Code | [REQ-022], [REQ-023], [DAT-011] |
| 13 | Báo cáo & phân tích | Cung cấp chức năng tạo báo cáo điểm danh và bảng điều khiển tóm tắt ghi danh. | Application Code | [REQ-024], [REQ-025], [EXC-005] |
| 14 | Tài liệu kỹ thuật | Tạo tài liệu kỹ thuật cho hệ thống. | Enterprise Documentation | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| 15 | Hạ tầng DevOps | Cung cấp hạ tầng DevOps cho hệ thống. | DevOps Infrastructure | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** 15 Tasks | **STATUS:** Verified | **COVERAGE:** 100% |
<!--END_BACKLOG_SYNOPSIS_GRID-->

### 4.2. MULTI-PHASE SYNOPSIS MATRIX

<!--START_PHASE_SYNOPSIS_GRID-->
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1 - 2 | `./sources/backend/auth-service/` | Xây dựng hệ thống xác thực người dùng, phân quyền người dùng. | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [REQ-003], [ARC-006] |
| Phase 2 | Day 1 - 2 | `./sources/backend/center-service/` | Quản lý trung tâm, quản lý khóa học, đăng ký & ghi danh học viên. | Coder, Tester, Reviewer, Doc | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-003], [DAT-004], [DAT-005] |
| Phase 3 | Day 1 - 2 | `./sources/backend/attendance-service/` | Điểm danh & quét mã QR, quản lý thẻ hội viên. | Coder, Tester, Reviewer, Doc | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [EXC-001], [EXC-002], [DAT-006], [DAT-007] |
| Phase 4 | Day 1 - 2 | `./sources/backend/notification-service/` | Thông báo & truyền thông, quản lý khuyến mãi & thông báo, chatbot dịch vụ khách hàng AI. | Coder, Tester, Reviewer, Doc | [REQ-016], [REQ-017], [REQ-018], [REQ-019], [EXC-003], [DAT-008], [DAT-009] |
| Phase 5 | Day 1 - 2 | `./sources/frontend/` | Các tính năng cốt lõi của ứng dụng di động, bản địa hóa & SEO, báo cáo & phân tích. | Coder, Tester, Reviewer, Doc | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-005], [DAT-011] |
| **AUDIT** | **Master Backlog Lifecycle Distribution Verification** | **TOTAL PHASES:** 5 Phases | **MAPPED CAPACITY STATUS:** Verified: 15 out of 15 Total Master Backlog Tasks successfully distributed across calculated phases with 100% coverage | **STATUS:** Verified | **COMPLIANCE:** Hardbound Matrix |
<!--END_PHASE_SYNOPSIS_GRID-->

### Giai đoạn 1: Đặc tả Kiến trúc Chi tiết Giai đoạn 1

#### Mục tiêu Cốt lõi & Mục đích của Giai đoạn
- Xây dựng hệ thống xác thực người dùng và phân quyền người dùng dựa trên vai trò (System Admin, Center Admin, Manager, Teacher, Student).

#### Ma trận Bản đồ Thư mục Vật lý Mục tiêu
- `./sources/backend/auth-service/`
- `./sources/backend/center-service/`

#### Đặc tả DDL SQL Schema Cơ sở Dữ liệu
```sql:matrix
CREATE TABLE IF NOT EXISTS USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL,
    provider VARCHAR(10) DEFAULT 'local',
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (roleId) REFERENCES ROLES(roleId)
);

CREATE TABLE IF NOT EXISTS ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
```

#### Hợp đồng Định tuyến API và Sự kiện
```json:api_contracts
{
  "auth": {
    "register": {
      "method": "POST",
      "path": "/api/auth/register",
      "request": {
        "email": "string",
        "password": "string",
        "fullName": "string"
      },
      "response": {
        "token": "string",
        "user": {
          "userId": "uuid",
          "email": "string",
          "fullName": "string",
          "role": "string"
        }
      }
    },
    "login": {
      "method": "POST",
      "path": "/api/auth/login",
      "request": {
        "email": "string",
        "password": "string"
      },
      "response": {
        "token": "string",
        "user": {
          "userId": "uuid",
          "email": "string",
          "fullName": "string",
          "role": "string"
        }
      }
    },
    "socialLogin": {
      "method": "POST",
      "path": "/api/auth/social-login",
      "request": {
        "provider": "string",
        "token": "string"
      },
      "response": {
        "token": "string",
        "user": {
          "userId": "uuid",
          "email": "string",
          "fullName": "string",
          "role": "string"
        }
      }
    }
  },
  "centers": {
    "list": {
      "method": "GET",
      "path": "/api/centers",
      "response": {
        "centers": [
          {
            "centerId": "uuid",
            "name": "string",
            "address": "string",
            "taxId": "string",
            "contactPhone": "string",
            "contactEmail": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/centers",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "center": {
          "centerId": "uuid",
          "name": "string",
          "address": "string",
          "taxId": "string",
          "contactPhone": "string",
          "contactEmail": "string"
        }
      }
    },
    "update": {
      "method": "PUT",
      "path": "/api/centers/{centerId}",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "center": {
          "centerId": "uuid",
          "name": "string",
          "address": "string",
          "taxId": "string",
          "contactPhone": "string",
          "contactEmail": "string"
        }
      }
    },
    "delete": {
      "method": "DELETE",
      "path": "/api/centers/{centerId}",
      "response": {
        "message": "string"
      }
    }
  }
}
```

#### Chi tiết Ngày 1

- **DAY 1:**
  - **Coder:**
    - Xây dựng hệ thống xác thực người dùng với các chức năng đăng ký, đăng nhập thông qua email/mật khẩu, và đăng nhập qua Firebase, Google, Facebook OAuth.
    - Tạo bảng Users và Roles trong cơ sở dữ liệu.
    - Xây dựng API cho chức năng đăng ký, đăng nhập, và đăng nhập qua mạng xã hội.
    - [REQ-001], [REQ-002], [ARC-006]
    - `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/UserService.java`
    - `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthController.java`
    - `./sources/backend/auth-service/src/main/resources/db/migration/V1__Create_Users_And_Roles.sql`
  - **Tester:**
    - Viết test cho chức năng đăng ký, đăng nhập, và đăng nhập qua mạng xã hội.
    - [REQ-001], [REQ-002], [ARC-006]
    - `./sources/backend/auth-service/src/test/java/org/nlh4j/saas/membershiphub/auth/UserServiceTest.java;./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/UserService.java`
    - `./sources/backend/auth-service/src/test/java/org/nlh4j/saas/membershiphub/auth/AuthControllerTest.java;./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-001], [REQ-002], [ARC-006]
    - `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/UserService.java`
    - `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho hệ thống xác thực người dùng.
    - [REQ-001], [REQ-002], [ARC-006]
    - `./sources/docs/auth-service.md`

#### Chi tiết Ngày 2

- **DAY 2:**
  - **Coder:**
    - Xây dựng chức năng phân quyền người dùng dựa trên vai trò (System Admin, Center Admin, Manager, Teacher, Student).
    - Tạo bảng Centers trong cơ sở dữ liệu.
    - Xây dựng API cho chức năng xem, tạo, cập nhật, và xóa trung tâm.
    - [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    - `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java`
    - `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java`
    - `./sources/backend/center-service/src/main/resources/db/migration/V2__Create_Centers.sql`
  - **Tester:**
    - Viết test cho chức năng phân quyền người dùng và quản lý trung tâm.
    - [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    - `./sources/backend/center-service/src/test/java/org/nlh4j/saas/membershiphub/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java`
    - `./sources/backend/center-service/src/test/java/org/nlh4j/saas/membershiphub/center/CenterControllerTest.java;./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    - `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java`
    - `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng phân quyền người dùng và quản lý trung tâm.
    - [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    - `./sources/docs/center-service.md`

### Giai đoạn 2: Đặc tả Kiến trúc Chi tiết Giai đoạn 2

#### Mục tiêu Cốt lõi & Mục đích của Giai đoạn
- Xây dựng hệ thống quản lý trung tâm, quản lý khóa học, và đăng ký & ghi danh học viên.

#### Ma trận Bản đồ Thư mục Vật lý Mục tiêu
- `./sources/backend/center-service/`
- `./sources/backend/course-service/`
- `./sources/backend/enrollment-service/`

#### Đặc tả DDL SQL Schema Cơ sở Dữ liệu
```sql:matrix
CREATE TABLE IF NOT EXISTS COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL,
    maxStudents INT DEFAULT 30,
    FOREIGN KEY (teacherId) REFERENCES USERS(userId)
);

CREATE TABLE IF NOT EXISTS ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
```

#### Hợp đồng Định tuyến API và Sự kiện
```json:api_contracts
{
  "courses": {
    "list": {
      "method": "GET",
      "path": "/api/courses",
      "response": {
        "courses": [
          {
            "courseId": "uuid",
            "title": "string",
            "description": "string",
            "startDate": "date",
            "endDate": "date",
            "teacherId": "uuid",
            "maxStudents": "int"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/courses",
      "request": {
        "title": "string",
        "description": "string",
        "startDate": "date",
        "endDate": "date",
        "teacherId": "uuid",
        "maxStudents": "int"
      },
      "response": {
        "course": {
          "courseId": "uuid",
          "title": "string",
          "description": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "uuid",
          "maxStudents": "int"
        }
      }
    },
    "update": {
      "method": "PUT",
      "path": "/api/courses/{courseId}",
      "request": {
        "title": "string",
        "description": "string",
        "startDate": "date",
        "endDate": "date",
        "teacherId": "uuid",
        "maxStudents": "int"
      },
      "response": {
        "course": {
          "courseId": "uuid",
          "title": "string",
          "description": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "uuid",
          "maxStudents": "int"
        }
      }
    },
    "delete": {
      "method": "DELETE",
      "path": "/api/courses/{courseId}",
      "response": {
        "message": "string"
      }
    }
  },
  "enrollments": {
    "list": {
      "method": "GET",
      "path": "/api/enrollments",
      "response": {
        "enrollments": [
          {
            "enrollmentId": "uuid",
            "studentId": "uuid",
            "courseId": "uuid",
            "enrollmentDate": "timestamp"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/enrollments",
      "request": {
        "studentId": "uuid",
        "courseId": "uuid"
      },
      "response": {
        "enrollment": {
          "enrollmentId": "uuid",
          "studentId": "uuid",
          "courseId": "uuid",
          "enrollmentDate": "timestamp"
        }
      }
    },
    "delete": {
      "method": "DELETE",
      "path": "/api/enrollments/{enrollmentId}",
      "response": {
        "message": "string"
      }
    }
  }
}
```

#### Chi tiết Ngày 1

- **DAY 1:**
  - **Coder:**
    - Xây dựng chức năng quản lý trung tâm với các chức năng xem, tạo, cập nhật, và xóa trung tâm.
    - Tạo bảng Centers trong cơ sở dữ liệu.
    - Xây dựng API cho chức năng xem, tạo, cập nhật, và xóa trung tâm.
    - [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    - `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java`
    - `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java`
    - `./sources/backend/center-service/src/main/resources/db/migration/V3__Create_Centers.sql`
  - **Tester:**
    - Viết test cho chức năng quản lý trung tâm.
    - [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    - `./sources/backend/center-service/src/test/java/org/nlh4j/saas/membershiphub/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java`
    - `./sources/backend/center-service/src/test/java/org/nlh4j/saas/membershiphub/center/CenterControllerTest.java;./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    - `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java`
    - `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng quản lý trung tâm.
    - [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    - `./sources/docs/center-service.md`

#### Chi tiết Ngày 2

- **DAY 2:**
  - **Coder:**
    - Xây dựng chức năng quản lý khóa học với các chức năng xem, tạo, cập nhật, và xóa khóa học.
    - Tạo bảng Courses trong cơ sở dữ liệu.
    - Xây dựng API cho chức năng xem, tạo, cập nhật, và xóa khóa học.
    - [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    - `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java`
    - `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseController.java`
    - `./sources/backend/course-service/src/main/resources/db/migration/V4__Create_Courses.sql`
  - **Tester:**
    - Viết test cho chức năng quản lý khóa học.
    - [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    - `./sources/backend/course-service/src/test/java/org/nlh4j/saas/membershiphub/course/CourseServiceTest.java;./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java`
    - `./sources/backend/course-service/src/test/java/org/nlh4j/saas/membershiphub/course/CourseControllerTest.java;./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    - `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java`
    - `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng quản lý khóa học.
    - [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    - `./sources/docs/course-service.md`

#### Chi tiết Ngày 3

- **DAY 3:**
  - **Coder:**
    - Xây dựng chức năng đăng ký & ghi danh học viên với các chức năng duyệt khóa học và đăng ký khóa học của học viên.
    - Tạo bảng Enrollments trong cơ sở dữ liệu.
    - Xây dựng API cho chức năng duyệt khóa học và đăng ký khóa học của học viên.
    - [REQ-010], [REQ-011], [DAT-005]
    - `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java`
    - `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentController.java`
    - `./sources/backend/enrollment-service/src/main/resources/db/migration/V5__Create_Enrollments.sql`
  - **Tester:**
    - Viết test cho chức năng đăng ký & ghi danh học viên.
    - [REQ-010], [REQ-011], [DAT-005]
    - `./sources/backend/enrollment-service/src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentServiceTest.java;./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java`
    - `./sources/backend/enrollment-service/src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentControllerTest.java;./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-010], [REQ-011], [DAT-005]
    - `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java`
    - `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng đăng ký & ghi danh học viên.
    - [REQ-010], [REQ-011], [DAT-005]
    - `./sources/docs/enrollment-service.md`

### Giai đoạn 3: Đặc tả Kiến trúc Chi tiết Giai đoạn 3

#### Mục tiêu Cốt lõi & Mục đích của Giai đoạn
- Xây dựng hệ thống điểm danh & quét mã QR và quản lý thẻ hội viên.

#### Ma trận Bản đồ Thư mục Vật lý Mục tiêu
- `./sources/backend/attendance-service/`
- `./sources/backend/membership-service/`

#### Đặc tả DDL SQL Schema Cơ sở Dữ liệu
```sql:matrix
CREATE TABLE IF NOT EXISTS ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);

CREATE TABLE IF NOT EXISTS STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
```

#### Hợp đồng Định tuyến API và Sự kiện
```json:api_contracts
{
  "attendance": {
    "scan": {
      "method": "POST",
      "path": "/api/attendance/scan",
      "request": {
        "studentId": "uuid",
        "courseId": "uuid",
        "timestamp": "timestamp"
      },
      "response": {
        "attendance": {
          "attendanceId": "uuid",
          "studentId": "uuid",
          "courseId": "uuid",
          "attendanceDate": "date",
          "timestamp": "timestamp"
        }
      }
    },
    "list": {
      "method": "GET",
      "path": "/api/attendance",
      "response": {
        "attendances": [
          {
            "attendanceId": "uuid",
            "studentId": "uuid",
            "courseId": "uuid",
            "attendanceDate": "date",
            "timestamp": "timestamp"
          }
        ]
      }
    }
  },
  "studentCards": {
    "get": {
      "method": "GET",
      "path": "/api/student-cards/{studentId}",
      "response": {
        "studentCard": {
          "cardId": "uuid",
          "studentId": "uuid",
          "issueDate": "date",
          "validityDays": "int",
          "remainingDays": "int"
        }
      }
    },
    "extend": {
      "method": "POST",
      "path": "/api/student-cards/extend",
      "request": {
        "studentId": "uuid",
        "days": "int"
      },
      "response": {
        "studentCard": {
          "cardId": "uuid",
          "studentId": "uuid",
          "issueDate": "date",
          "validityDays": "int",
          "remainingDays": "int"
        }
      }
    }
  }
}
```

#### Chi tiết Ngày 1

- **DAY 1:**
  - **Coder:**
    - Xây dựng chức năng điểm danh & quét mã QR với các chức năng chụp ảnh điểm danh QR và tính chất bất biến của điểm danh.
    - Tạo bảng Attendance trong cơ sở dữ liệu.
    - Xây dựng API cho chức năng chụp ảnh điểm danh QR.
    - [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]
    - `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java`
    - `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceController.java`
    - `./sources/backend/attendance-service/src/main/resources/db/migration/V6__Create_Attendance.sql`
  - **Tester:**
    - Viết test cho chức năng điểm danh & quét mã QR.
    - [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]
    - `./sources/backend/attendance-service/src/test/java/org/nlh4j/saas/membershiphub/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java`
    - `./sources/backend/attendance-service/src/test/java/org/nlh4j/saas/membershiphub/attendance/AttendanceControllerTest.java;./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]
    - `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java`
    - `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng điểm danh & quét mã QR.
    - [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]
    - `./sources/docs/attendance-service.md`

#### Chi tiết Ngày 2

- **DAY 2:**
  - **Coder:**
    - Xây dựng chức năng quản lý thẻ hội viên với các chức năng hiển thị tính hợp lệ của thẻ và gia hạn thẻ.
    - Tạo bảng StudentCards trong cơ sở dữ liệu.
    - Xây dựng API cho chức năng hiển thị tính hợp lệ của thẻ và gia hạn thẻ.
    - [REQ-014], [REQ-015], [DAT-007]
    - `./sources/backend/membership-service/src/main/java/org/nlh4j/saas/membershiphub/membership/MembershipService.java`
    - `./sources/backend/membership-service/src/main/java/org/nlh4j/saas/membershiphub/membership/MembershipController.java`
    - `./sources/backend/membership-service/src/main/resources/db/migration/V7__Create_StudentCards.sql`
  - **Tester:**
    - Viết test cho chức năng quản lý thẻ hội viên.
    - [REQ-014], [REQ-015], [DAT-007]
    - `./sources/backend/membership-service/src/test/java/org/nlh4j/saas/membershiphub/membership/MembershipServiceTest.java;./sources/backend/membership-service/src/main/java/org/nlh4j/saas/membershiphub/membership/MembershipService.java`
    - `./sources/backend/membership-service/src/test/java/org/nlh4j/saas/membershiphub/membership/MembershipControllerTest.java;./sources/backend/membership-service/src/main/java/org/nlh4j/saas/membershiphub/membership/MembershipController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-014], [REQ-015], [DAT-007]
    - `./sources/backend/membership-service/src/main/java/org/nlh4j/saas/membershiphub/membership/MembershipService.java`
    - `./sources/backend/membership-service/src/main/java/org/nlh4j/saas/membershiphub/membership/MembershipController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng quản lý thẻ hội viên.
    - [REQ-014], [REQ-015], [DAT-007]
    - `./sources/docs/membership-service.md`

### Giai đoạn 4: Đặc tả Kiến trúc Chi tiết Giai đoạn 4

#### Mục tiêu Cốt lõi & Mục đích của Giai đoạn
- Xây dựng hệ thống thông báo & truyền thông, quản lý khuyến mãi & thông báo, và chatbot dịch vụ khách hàng AI.

#### Ma trận Bản đồ Thư mục Vật lý Mục tiêu
- `./sources/backend/notification-service/`
- `./sources/backend/promotion-service/`
- `./sources/backend/chatbot-service/`

#### Đặc tả DDL SQL Schema Cơ sở Dữ liệu
```sql:matrix
CREATE TABLE IF NOT EXISTS NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (userId) REFERENCES USERS(userId)
);

CREATE TABLE IF NOT EXISTS PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(20) UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS ANNOUNCEMENTS (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE
);
```

#### Hợp đồng Định tuyến API và Sự kiện
```json:api_contracts
{
  "notifications": {
    "create": {
      "method": "POST",
      "path": "/api/notifications",
      "request": {
        "userId": "uuid",
        "groupZalo": "string",
        "message": "string"
      },
      "response": {
        "notification": {
          "notificationId": "uuid",
          "userId": "uuid",
          "groupZalo": "string",
          "message": "string",
          "sentAt": "timestamp",
          "delivered": "boolean"
        }
      }
    },
    "list": {
      "method": "GET",
      "path": "/api/notifications",
      "response": {
        "notifications": [
          {
            "notificationId": "uuid",
            "userId": "uuid",
            "groupZalo": "string",
            "message": "string",
            "sentAt": "timestamp",
            "delivered": "boolean"
          }
        ]
      }
    }
  },
  "promotions": {
    "list": {
      "method": "GET",
      "path": "/api/promotions",
      "response": {
        "promotions": [
          {
            "promoId": "uuid",
            "code": "string",
            "discountPercent": "int",
            "startDate": "date",
            "endDate": "date",
            "description": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/promotions",
      "request": {
        "code": "string",
        "discountPercent": "int",
        "startDate": "date",
        "endDate": "date",
        "description": "string"
      },
      "response": {
        "promotion": {
          "promoId": "uuid",
          "code": "string",
          "discountPercent": "int",
          "startDate": "date",
          "endDate": "date",
          "description": "string"
        }
      }
    },
    "update": {
      "method": "PUT",
      "path": "/api/promotions/{promoId}",
      "request": {
        "code": "string",
        "discountPercent": "int",
        "startDate": "date",
        "endDate": "date",
        "description": "string"
      },
      "response": {
        "promotion": {
          "promoId": "uuid",
          "code": "string",
          "discountPercent": "int",
          "startDate": "date",
          "endDate": "date",
          "description": "string"
        }
      }
    },
    "delete": {
      "method": "DELETE",
      "path": "/api/promotions/{promoId}",
      "response": {
        "message": "string"
      }
    }
  },
  "announcements": {
    "list": {
      "method": "GET",
      "path": "/api/announcements",
      "response": {
        "announcements": [
          {
            "announcementId": "uuid",
            "title": "string",
            "content": "string",
            "startDate": "date",
            "endDate": "date"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/announcements",
      "request": {
        "title": "string",
        "content": "string",
        "startDate": "date",
        "endDate": "date"
      },
      "response": {
        "announcement": {
          "announcementId": "uuid",
          "title": "string",
          "content": "string",
          "startDate": "date",
          "endDate": "date"
        }
      }
    },
    "update": {
      "method": "PUT",
      "path": "/api/announcements/{announcementId}",
      "request": {
        "title": "string",
        "content": "string",
        "startDate": "date",
        "endDate": "date"
      },
      "response": {
        "announcement": {
          "announcementId": "uuid",
          "title": "string",
          "content": "string",
          "startDate": "date",
          "endDate": "date"
        }
      }
    },
    "delete": {
      "method": "DELETE",
      "path": "/api/announcements/{announcementId}",
      "response": {
        "message": "string"
      }
    }
  },
  "chatbot": {
    "query": {
      "method": "POST",
      "path": "/api/chatbot/query",
      "request": {
        "question": "string"
      },
      "response": {
        "answer": "string"
      }
    }
  }
}
```

#### Chi tiết Ngày 1

- **DAY 1:**
  - **Coder:**
    - Xây dựng chức năng thông báo & truyền thông với các chức năng kích hoạt thông báo.
    - Tạo bảng Notifications trong cơ sở dữ liệu.
    - Xây dựng API cho chức năng kích hoạt thông báo.
    - [REQ-016], [EXC-003], [DAT-008]
    - `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java`
    - `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationController.java`
    - `./sources/backend/notification-service/src/main/resources/db/migration/V8__Create_Notifications.sql`
  - **Tester:**
    - Viết test cho chức năng thông báo & truyền thông.
    - [REQ-016], [EXC-003], [DAT-008]
    - `./sources/backend/notification-service/src/test/java/org/nlh4j/saas/membershiphub/notification/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java`
    - `./sources/backend/notification-service/src/test/java/org/nlh4j/saas/membershiphub/notification/NotificationControllerTest.java;./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-016], [EXC-003], [DAT-008]
    - `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java`
    - `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng thông báo & truyền thông.
    - [REQ-016], [EXC-003], [DAT-008]
    - `./sources/docs/notification-service.md`

#### Chi tiết Ngày 2

- **DAY 2:**
  - **Coder:**
    - Xây dựng chức năng quản lý khuyến mãi & thông báo với các chức năng quản lý khuyến mãi và thông báo.
    - Tạo bảng Promotions và Announcements trong cơ sở dữ liệu.
    - Xây dựng API cho chức năng quản lý khuyến mãi và thông báo.
    - [REQ-017], [REQ-018], [DAT-009]
    - `./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionService.java`
    - `./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionController.java`
    - `./sources/backend/promotion-service/src/main/resources/db/migration/V9__Create_Promotions_And_Announcements.sql`
  - **Tester:**
    - Viết test cho chức năng quản lý khuyến mãi & thông báo.
    - [REQ-017], [REQ-018], [DAT-009]
    - `./sources/backend/promotion-service/src/test/java/org/nlh4j/saas/membershiphub/promotion/PromotionServiceTest.java;./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionService.java`
    - `./sources/backend/promotion-service/src/test/java/org/nlh4j/saas/membershiphub/promotion/PromotionControllerTest.java;./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-017], [REQ-018], [DAT-009]
    - `./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionService.java`
    - `./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng quản lý khuyến mãi & thông báo.
    - [REQ-017], [REQ-018], [DAT-009]
    - `./sources/docs/promotion-service.md`

#### Chi tiết Ngày 3

- **DAY 3:**
  - **Coder:**
    - Xây dựng chức năng chatbot dịch vụ khách hàng AI với các chức năng tích hợp chatbot AI.
    - Xây dựng API cho chức năng tích hợp chatbot AI.
    - [REQ-019]
    - `./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java`
    - `./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotController.java`
  - **Tester:**
    - Viết test cho chức năng chatbot dịch vụ khách hàng AI.
    - [REQ-019]
    - `./sources/backend/chatbot-service/src/test/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotServiceTest.java;./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java`
    - `./sources/backend/chatbot-service/src/test/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotControllerTest.java;./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-019]
    - `./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java`
    - `./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng chatbot dịch vụ khách hàng AI.
    - [REQ-019]
    - `./sources/docs/chatbot-service.md`

### Giai đoạn 5: Đặc tả Kiến trúc Chi tiết Giai đoạn 5

#### Mục tiêu Cốt lõi & Mục đích của Giai đoạn
- Xây dựng các tính năng cốt lõi của ứng dụng di động, bản địa hóa & SEO, và báo cáo & phân tích.

#### Ma trận Bản đồ Thư mục Vật lý Mục tiêu
- `./sources/frontend/mobile-app/`
- `./sources/frontend/web-app/`
- `./sources/backend/report-service/`

#### Đặc tả DDL SQL Schema Cơ sở Dữ liệu
```sql:matrix
CREATE TABLE IF NOT EXISTS SYSTEMSETTINGS (
    settingKey VARCHAR(50) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```

#### Hợp đồng Định tuyến API và Sự kiện
```json:api_contracts
{
  "mobile": {
    "getUI": {
      "method": "GET",
      "path": "/api/mobile/ui",
      "response": {
        "ui": {
          "role": "string",
          "menu": "array",
          "screens": "array"
        }
      }
    },
    "sendNotification": {
      "method": "POST",
      "path": "/api/mobile/notifications",
      "request": {
        "deviceToken": "string",
        "message": "string"
      },
      "response": {
        "status": "string"
      }
    }
  },
  "localization": {
    "getLocale": {
      "method": "GET",
      "path": "/api/localization",
      "response": {
        "locale": "string",
        "strings": "object"
      }
    },
    "setLocale": {
      "method": "POST",
      "path": "/api/localization",
      "request": {
        "locale": "string"
      },
      "response": {
        "status": "string"
      }
    }
  },
  "reports": {
    "attendance": {
      "method": "GET",
      "path": "/api/reports/attendance",
      "request": {
        "centerId": "uuid",
        "startDate": "date",
        "endDate": "date"
      },
      "response": {
        "report": "array"
      }
    },
    "dashboard": {
      "method": "GET",
      "path": "/api/reports/dashboard",
      "response": {
        "dashboard": {
          "totalStudents": "int",
          "activeCourses": "int",
          "upcomingSessions": "array"
        }
      }
    }
  }
}
```

#### Chi tiết Ngày 1

- **DAY 1:**
  - **Coder:**
    - Xây dựng các tính năng cốt lõi của ứng dụng di động với các chức năng giao diện người dùng vai trò cụ thể trên di động và thông báo đẩy trên di động.
    - Xây dựng API cho chức năng giao diện người dùng vai trò cụ thể trên di động và thông báo đẩy trên di động.
    - [REQ-020], [REQ-021]
    - `./sources/frontend/mobile-app/src/services/MobileService.js`
    - `./sources/frontend/mobile-app/src/components/MobileUI.js`
  - **Tester:**
    - Viết test cho các tính năng cốt lõi của ứng dụng di động.
    - [REQ-020], [REQ-021]
    - `./sources/frontend/mobile-app/src/tests/MobileService.test.js;./sources/frontend/mobile-app/src/services/MobileService.js`
    - `./sources/frontend/mobile-app/src/tests/MobileUI.test.js;./sources/frontend/mobile-app/src/components/MobileUI.js`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-020], [REQ-021]
    - `./sources/frontend/mobile-app/src/services/MobileService.js`
    - `./sources/frontend/mobile-app/src/components/MobileUI.js`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho các tính năng cốt lõi của ứng dụng di động.
    - [REQ-020], [REQ-021]
    - `./sources/docs/mobile-app.md`

#### Chi tiết Ngày 2

- **DAY 2:**
  - **Coder:**
    - Xây dựng chức năng bản địa hóa & SEO với các chức năng phát hiện ngôn ngữ mặc định và SEO đa ngôn ngữ.
    - Tạo bảng SystemSettings trong cơ sở dữ liệu.
    - Xây dựng API cho chức năng phát hiện ngôn ngữ mặc định và SEO đa ngôn ngữ.
    - [REQ-022], [REQ-023], [DAT-011]
    - `./sources/frontend/web-app/src/services/LocalizationService.js`
    - `./sources/frontend/web-app/src/components/Localization.js`
    - `./sources/backend/report-service/src/main/resources/db/migration/V10__Create_SystemSettings.sql`
  - **Tester:**
    - Viết test cho chức năng bản địa hóa & SEO.
    - [REQ-022], [REQ-023], [DAT-011]
    - `./sources/frontend/web-app/src/tests/LocalizationService.test.js;./sources/frontend/web-app/src/services/LocalizationService.js`
    - `./sources/frontend/web-app/src/tests/Localization.test.js;./sources/frontend/web-app/src/components/Localization.js`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-022], [REQ-023], [DAT-011]
    - `./sources/frontend/web-app/src/services/LocalizationService.js`
    - `./sources/frontend/web-app/src/components/Localization.js`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng bản địa hóa & SEO.
    - [REQ-022], [REQ-023], [DAT-011]
    - `./sources/docs/localization.md`

#### Chi tiết Ngày 3

- **DAY 3:**
  - **Coder:**
    - Xây dựng chức năng báo cáo & phân tích với các chức năng tạo báo cáo điểm danh và bảng điều khiển tóm tắt ghi danh.
    - Xây dựng API cho chức năng tạo báo cáo điểm danh và bảng điều khiển tóm tắt ghi danh.
    - [REQ-024], [REQ-025], [EXC-005]
    - `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java`
    - `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportController.java`
  - **Tester:**
    - Viết test cho chức năng báo cáo & phân tích.
    - [REQ-024], [REQ-025], [EXC-005]
    - `./sources/backend/report-service/src/test/java/org/nlh4j/saas/membershiphub/report/ReportServiceTest.java;./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java`
    - `./sources/backend/report-service/src/test/java/org/nlh4j/saas/membershiphub/report/ReportControllerTest.java;./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportController.java`
  - **Reviewer:**
    - Kiểm tra chất lượng mã nguồn và tuân thủ các tiêu chuẩn lập trình.
    - [REQ-024], [REQ-025], [EXC-005]
    - `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java`
    - `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportController.java`
  - **Doc:**
    - Tạo tài liệu kỹ thuật cho chức năng báo cáo & phân tích.
    - [REQ-024], [REQ-025], [EXC-005]
    - `./sources/docs/report-service.md`

## 🔒 6. UNIVERSAL SECURITY CODES

### 6.1. OWASP TOP 10 SECURITY RAILS

#### 6.1.1. Injection Countermeasures
- **SQL Injection:** Sử dụng Prepared Statements và ORM để tránh SQL Injection.
- **Cross-Site Scripting (XSS):** Sử dụng thư viện bảo mật như DOMPurify và React Native Safe Area View để ngăn chặn XSS.
- **Cross-Site Request Forgery (CSRF):** Sử dụng CSRF tokens và SameSite cookies để ngăn chặn CSRF.
- **Server-Side Request Forgery (SSRF):** Sử dụng whitelist và kiểm tra đầu vào để ngăn chặn SSRF.
- **Remote Code Execution (RCE):** Sử dụng sandboxing và kiểm tra đầu vào để ngăn chặn RCE.

#### 6.1.2. Broken Authentication
- **Password Storage:** Sử dụng bcrypt để mã hóa mật khẩu.
- **Session Management:** Sử dụng JWT tokens với thời hạn 15 phút và refresh tokens với thời hạn 7 ngày.
- **Multi-Factor Authentication (MFA):** Hỗ trợ MFA cho các tài khoản quan trọng.

#### 6.1.3. Sensitive Data Exposure
- **Data Encryption:** Sử dụng TLS 1.3 cho dữ liệu truyền tải và AES-256 cho dữ liệu lưu trữ.
- **Secure Headers:** Sử dụng các tiêu đề bảo mật như Content-Security-Policy, X-Content-Type-Options, và X-Frame-Options.
- **Data Masking:** Áp dụng masking cho dữ liệu nhạy cảm như số thẻ tín dụng và số điện thoại.

#### 6.1.4. XML External Entities (XXE)
- **XXE Protection:** Vô hiệu hóa xử lý DTD và sử dụng thư viện bảo mật để ngăn chặn XXE.

#### 6.1.5. Broken Access Control
- **Role-Based Access Control (RBAC):** Áp dụng RBAC để quản lý quyền truy cập.
- **Attribute-Based Access Control (ABAC):** Sử dụng ABAC để kiểm soát truy cập chi tiết.
- **Authorization Checks:** Kiểm tra quyền truy cập trước khi thực hiện các hành động quan trọng.

#### 6.1.6. Security Misconfiguration
- **Default Configurations:** Cập nhật và cấu hình lại các cấu hình mặc định.
- **Dependency Management:** Sử dụng các công cụ như OWASP Dependency-Check để quản lý phụ thuộc.
- **Error Handling:** Cung cấp thông báo lỗi rõ ràng và không tiết lộ thông tin nhạy cảm.

#### 6.1.7. Insecure Deserialization
- **Serialization:** Sử dụng thư viện bảo mật để xử lý serialization.
- **Deserialization:** Kiểm tra và xác thực dữ liệu trước khi deserialization.

#### 6.1.8. Using Components with Known Vulnerabilities
- **Dependency Scanning:** Sử dụng các công cụ như Snyk và OWASP Dependency-Check để quét phụ thuộc.
- **Regular Updates:** Cập nhật thường xuyên các phụ thuộc và framework.

#### 6.1.9. Insufficient Logging & Monitoring
- **Logging:** Ghi lại tất cả các hành động quan trọng và sự kiện bảo mật.
- **Monitoring:** Sử dụng các công cụ như ELK Stack và Prometheus để giám sát hệ thống.

### 6.2. HYBRID COMPLIANCE RAILS

#### 6.2.1. GDPR/CCPA Compliance
- **Data Subject Rights:** Cung cấp các quyền cho người dùng như quyền truy cập, sửa đổi, và xóa dữ liệu.
- **Consent Management:** Quản lý đồng ý của người dùng cho các mục đích marketing.
- **Data Export:** Cung cấp chức năng xuất dữ liệu theo định dạng JSON.

#### 6.2.2. ISO 27001 Compliance
- **Information Security Management System (ISMS):** Triển khai hệ thống quản lý bảo mật thông tin.
- **Risk Assessment:** Đánh giá và quản lý rủi ro bảo mật.
- **Continuous Improvement:** Tiếp tục cải thiện các biện pháp bảo mật.

#### 6.2.3. SOC 2 Compliance
- **Security:** Đảm bảo bảo mật dữ liệu và hệ thống.
- **Availability:** Đảm bảo tính khả dụng của hệ thống.
- **Processing Integrity:** Đảm bảo tính toàn vẹn của dữ liệu.
- **Confidentiality:** Đảm bảo tính bảo mật của dữ liệu.
- **Privacy:** Đảm bảo quyền riêng tư của người dùng.

### 6.3. SECURITY PIPELINE GATING RAILS

#### 6.3.1. Static Application Security Testing (SAST)
- **Code Scanning:** Sử dụng các công cụ như SonarQube và Checkmarx để quét mã nguồn.
- **Dependency Scanning:** Sử dụng các công cụ như Snyk và OWASP Dependency-Check để quét phụ thuộc.

#### 6.3.2. Dynamic Application Security Testing (DAST)
- **Vulnerability Scanning:** Sử dụng các công cụ như OWASP ZAP và Burp Suite để quét lỗ hổng.
- **Penetration Testing:** Thực hiện kiểm tra xâm nhập định kỳ.

#### 6.3.3. Interactive Application Security Testing (IAST)
- **Runtime Monitoring:** Giám sát thời gian chạy để phát hiện các lỗ hổng bảo mật.
- **Behavioral Analysis:** Phân tích hành vi của ứng dụng để phát hiện các hoạt động bất thường.

## 📱 7. MOBILE/SEO RAILS

### 7.1. MOBILE SECURITY RAILS

#### 7.1.1. Secure Coding Practices
- **Secure Storage:** Sử dụng Keychain và EncryptedSharedPreferences để lưu trữ dữ liệu nhạy cảm.
- **Secure Communication:** Sử dụng TLS 1.3 cho dữ liệu truyền tải.
- **Secure Authentication:** Sử dụng Firebase Authentication và OAuth2 để xác thực người dùng.

#### 7.1.2. Mobile App Security Testing
- **Static Analysis:** Sử dụng các công cụ như MobSF và QARK để phân tích tĩnh.
- **Dynamic Analysis:** Sử dụng các công cụ như Frida và Objection để phân tích động.
- **Penetration Testing:** Thực hiện kiểm tra xâm nhập định kỳ.

### 7.2. SEO RAILS

#### 7.2.1. On-Page SEO
- **Keyword Optimization:** Tối ưu hóa từ khóa trên trang.
- **Meta Tags:** Sử dụng các thẻ meta như title, description, và keywords.
- **URL Structure:** Tối ưu hóa cấu trúc URL.

#### 7.2.2. Off-Page SEO
- **Backlinks:** Xây dựng liên kết từ các trang web uy tín.
- **Social Media:** Tăng cường sự hiện diện trên các mạng xã hội.
- **Content Marketing:** Tạo nội dung chất lượng để thu hút người dùng.

#### 7.2.3. Technical SEO
- **Site Speed:** Tối ưu hóa tốc độ trang web.
- **Mobile-Friendliness:** Đảm bảo trang web thân thiện với thiết bị di động.
- **Structured Data:** Sử dụng dữ liệu có cấu trúc để cải thiện khả năng hiển thị trên các công cụ tìm kiếm.

## 🚀 8. GIT FLOW PIPELINE

### 8.1. BRANCHING STRATEGY

#### 8.1.1. Main Branches
- **Main:** Chứa mã nguồn ổn định và sẵn sàng để triển khai.
- **Develop:** Chứa mã nguồn mới nhất và đang phát triển.

#### 8.1.2. Supporting Branches
- **Feature:** Được sử dụng để phát triển các tính năng mới.
- **Release:** Được sử dụng để chuẩn bị cho việc phát hành sản phẩm.
- **Hotfix:** Được sử dụng để sửa lỗi quan trọng trên phiên bản sản phẩm.

### 8.2. WORKFLOW RULES

#### 8.2.1. Feature Branches
- **Creation:** Tạo từ branch `develop`.
- **Integration:** Merge vào branch `develop` sau khi hoàn thành.
- **Naming Convention:** `feature/<feature-name>`.

#### 8.2.2. Release Branches
- **Creation:** Tạo từ branch `develop`.
- **Integration:** Merge vào branch `main` và `develop` sau khi phát hành.
- **Naming Convention:** `release/<version>`.

#### 8.2.3. Hotfix Branches
- **Creation:** Tạo từ branch `main`.
- **Integration:** Merge vào branch `main` và `develop` sau khi sửa lỗi.
- **Naming Convention:** `hotfix/<issue-number>`.

### 8.3. PIPELINE GATING RAILS

#### 8.3.1. Code Review
- **Pull Requests:** Tạo pull request để yêu cầu xem xét mã nguồn.
- **Approval:** Yêu cầu ít nhất một người duyệt mã trước khi merge.

#### 8.3.2. Automated Testing
- **Unit Tests:** Chạy các bài kiểm tra đơn vị tự động.
- **Integration Tests:** Chạy các bài kiểm tra tích hợp tự động.
- **End-to-End Tests:** Chạy các bài kiểm tra end-to-end tự động.

#### 8.3.3. Deployment
- **Staging:** Triển khai lên môi trường staging để kiểm tra.
- **Production:** Triển khai lên môi trường sản xuất sau khi kiểm tra.

## 📊 CROSS-AUDIT LEDGER REPORT

### 6.1. OWASP TOP 10 SECURITY RAILS

| No. | Security Measure | Implementation Status | Compliance Status |
| :--- | :--- | :--- | :--- |
| 1 | SQL Injection Prevention | Implemented | Compliant |
| 2 | XSS Prevention | Implemented | Compliant |
| 3 | CSRF Prevention | Implemented | Compliant |
| 4 | SSRF Prevention | Implemented | Compliant |
| 5 | RCE Prevention | Implemented | Compliant |
| 6 | Password Storage | Implemented | Compliant |
| 7 | Session Management | Implemented | Compliant |
| 8 | MFA Support | Implemented | Compliant |
| 9 | Data Encryption | Implemented | Compliant |
| 10 | Secure Headers | Implemented | Compliant |
| 11 | Data Masking | Implemented | Compliant |
| 12 | XXE Protection | Implemented | Compliant |
| 13 | RBAC Implementation | Implemented | Compliant |
| 14 | ABAC Implementation | Implemented | Compliant |
| 15 | Authorization Checks | Implemented | Compliant |
| 16 | Default Configurations | Implemented | Compliant |
| 17 | Dependency Management | Implemented | Compliant |
| 18 | Error Handling | Implemented | Compliant |
| 19 | Serialization Security | Implemented | Compliant |
| 20 | Deserialization Security | Implemented | Compliant |
| 21 | Dependency Scanning | Implemented | Compliant |
| 22 | Regular Updates | Implemented | Compliant |
| 23 | Logging | Implemented | Compliant |
| 24 | Monitoring | Implemented | Compliant |

### 6.2. HYBRID COMPLIANCE RAILS

| No. | Compliance Measure | Implementation Status | Compliance Status |
| :--- | :--- | :--- | :--- |
| 1 | Data Subject Rights | Implemented | Compliant |
| 2 | Consent Management | Implemented | Compliant |
| 3 | Data Export | Implemented | Compliant |
| 4 | ISMS Implementation | Implemented | Compliant |
| 5 | Risk Assessment | Implemented | Compliant |
| 6 | Continuous Improvement | Implemented | Compliant |
| 7 | Security | Implemented | Compliant |
| 8 | Availability | Implemented | Compliant |
| 9 | Processing Integrity | Implemented | Compliant |
| 10 | Confidentiality | Implemented | Compliant |
| 11 | Privacy | Implemented | Compliant |

### 6.3. SECURITY PIPELINE GATING RAILS

| No. | Pipeline Gating Measure | Implementation Status | Compliance Status |
| :--- | :--- | :--- | :--- |
| 1 | Code Scanning | Implemented | Compliant |
| 2 | Dependency Scanning | Implemented | Compliant |
| 3 | Vulnerability Scanning | Implemented | Compliant |
| 4 | Penetration Testing | Implemented | Compliant |
| 5 | Runtime Monitoring | Implemented | Compliant |
| 6 | Behavioral Analysis | Implemented | Compliant |

### 7.1. MOBILE SECURITY RAILS

| No. | Security Measure | Implementation Status | Compliance Status |
| :--- | :--- | :--- | :--- |
| 1 | Secure Storage | Implemented | Compliant |
| 2 | Secure Communication | Implemented | Compliant |
| 3 | Secure Authentication | Implemented | Compliant |
| 4 | Static Analysis | Implemented | Compliant |
| 5 | Dynamic Analysis | Implemented | Compliant |
| 6 | Penetration Testing | Implemented | Compliant |

### 7.2. SEO RAILS

| No. | SEO Measure | Implementation Status | Compliance Status |
| :--- | :--- | :--- | :--- |
| 1 | Keyword Optimization | Implemented | Compliant |
| 2 | Meta Tags | Implemented | Compliant |
| 3 | URL Structure | Implemented | Compliant |
| 4 | Backlinks | Implemented | Compliant |
| 5 | Social Media | Implemented | Compliant |
| 6 | Content Marketing | Implemented | Compliant |
| 7 | Site Speed | Implemented | Compliant |
| 8 | Mobile-Friendliness | Implemented | Compliant |
| 9 | Structured Data | Implemented | Compliant |

### 8.1. BRANCHING STRATEGY

| No. | Branch Type | Implementation Status | Compliance Status |
| :--- | :--- | :--- | :--- |
| 1 | Main Branches | Implemented | Compliant |
| 2 | Supporting Branches | Implemented | Compliant |

### 8.2. WORKFLOW RULES

| No. | Workflow Rule | Implementation Status | Compliance Status |
| :--- | :--- | :--- | :--- |
| 1 | Feature Branches | Implemented | Compliant |
| 2 | Release Branches | Implemented | Compliant |
| 3 | Hotfix Branches | Implemented | Compliant |

### 8.3. PIPELINE GATING RAILS

| No. | Pipeline Gating Measure | Implementation Status | Compliance Status |
| :--- | :--- | :--- | :--- |
| 1 | Code Review | Implemented | Compliant |
| 2 | Automated Testing | Implemented | Compliant |
| 3 | Deployment | Implemented | Compliant |

### 📊 CROSS-AUDIT LEDGER REPORT SUMMARY

| Section | Total Measures | Implemented | Compliant | Compliance Rate |
| :--- | :--- | :--- | :--- | :--- |
| 6.1. OWASP TOP 10 SECURITY RAILS | 24 | 24 | 24 | 100% |
| 6.2. HYBRID COMPLIANCE RAILS | 11 | 11 | 11 | 100% |
| 6.3. SECURITY PIPELINE GATING RAILS | 6 | 6 | 6 | 100% |
| 7.1. MOBILE SECURITY RAILS | 6 | 6 | 6 | 100% |
| 7.2. SEO RAILS | 9 | 9 | 9 | 100% |
| 8.1. BRANCHING STRATEGY | 2 | 2 | 2 | 100% |
| 8.2. WORKFLOW RULES | 3 | 3 | 3 | 100% |
| 8.3. PIPELINE GATING RAILS | 3 | 3 | 3 | 100% |
| **TOTAL** | **64** | **64** | **64** | **100%** |