# ErgoDocsAgent Architecture Diagrams

This document contains visual representations of the ErgoDocsAgent architecture, workflow, and components.

## Component Architecture

```mermaid
graph TD
    A[ErgoDocsAgent] --> B[Configuration]
    A --> C[Ingestion]
    A --> D[Processing]
    A --> E[Output]
    A --> F[Scheduling]
    
    B --> B1[config.json]
    B --> B2[.env]
    
    C --> C1[GitHub Ingestion]
    C --> C2[Website Ingestion]
    
    D --> D1[Extractor]
    D --> D2[Transformer]
    
    E --> E1[Documentation Generator]
    
    F --> F1[Job Scheduler]
    
    C1 --> D1
    C2 --> D1
    D1 --> D2
    D2 --> E1
```

## Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant Main
    participant Ingestion
    participant Extractor
    participant Transformer
    participant Generator
    participant Scheduler
    
    User->>Main: Run with arguments
    Main->>Main: Load configuration
    
    alt Scheduled Mode
        Main->>Scheduler: Create scheduler
        Scheduler->>Main: Schedule pipeline execution
    else Direct Execution
        Main->>Main: Execute pipeline
    end
    
    Main->>Ingestion: Fetch content (GitHub/Website)
    Ingestion->>Main: Return raw content
    
    Main->>Extractor: Extract information
    Extractor->>Main: Return structured data
    
    Main->>Transformer: Transform with OpenAI
    Transformer->>Main: Return LLM-optimized content
    
    Main->>Generator: Generate documentation
    Generator->>Main: Output files created
    
    Main->>User: Complete execution
```

## Process Flow

```mermaid
flowchart TD
    A[Start] --> B{Parse Arguments}
    B --> |--config| C[Load Configuration]
    B --> |--source| D[Filter Sources]
    B --> |--schedule| E[Run Scheduled]
    B --> |--now| F[Run Immediately]
    
    C --> G[Process Sources]
    D --> G
    E --> H[Create Scheduler]
    F --> G
    
    G --> I{Source Type?}
    I --> |GitHub| J[GitHub Ingestion]
    I --> |Website| K[Website Ingestion]
    
    J --> L[Extract Content]
    K --> L
    
    L --> M[Transform with OpenAI]
    M --> N[Generate Output Files]
    
    H --> O[Schedule Jobs]
    O --> G
    
    N --> P[Log Completion]
    P --> Q[End]
```

## Class Diagram

```mermaid
classDiagram
    class GitHubIngestion {
        +url: string
        +branch: string
        +description: string
        +fetch()
    }
    
    class WebsiteIngestion {
        +url: string
        +max_depth: int
        +description: string
        +fetch()
    }
    
    class Extractor {
        +content: dict
        +extract()
        -_extract_sections()
        -_extract_code_samples()
    }
    
    class Transformer {
        +extracted_data: dict
        +api_key: string
        +model: string
        +transform()
        -_transform_document()
        -_generate_improved_summary()
        -_generate_qa_pairs()
        -_transform_sections()
    }
    
    class DocumentationGenerator {
        +transformed_data: dict
        +output_config: dict
        +source_description: string
        +generate()
        -_generate_markdown()
        -_generate_json()
        -_generate_qa_file()
        -_generate_combined_file()
    }
    
    class JobScheduler {
        +config: dict
        +add_job()
        +start()
        +stop()
    }
    
    GitHubIngestion ..> Extractor
    WebsiteIngestion ..> Extractor
    Extractor ..> Transformer
    Transformer ..> DocumentationGenerator
    JobScheduler --> GitHubIngestion
    JobScheduler --> WebsiteIngestion
``` 