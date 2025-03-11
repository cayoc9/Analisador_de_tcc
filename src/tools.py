from crewai.tools import BaseTool
from docling.document_converter import DocumentConverter
from pydantic import BaseModel, Field
from typing import Type, Optional
import os

class DoclingToolInput(BaseModel):
    """Esquema de entrada para a ferramenta de conversão de PDF."""
    query: Optional[str] = Field(None, description="Consulta para extração do PDF")

class DoclingTool(BaseTool):
    name: str = "Docling PDF Converter"
    description: str = "Converte PDFs em Markdown para análise e extração de informações."
    args_schema: Type[BaseModel] = DoclingToolInput

    def __init__(self, file_path: Optional[str] = None, **kwargs):
        """Inicializa a ferramenta e armazena o caminho do arquivo, se fornecido."""
        super().__init__(**kwargs)
        self.file_path = None
        if file_path:
            self.add(file_path)  # Adiciona o caminho do PDF

    def add(self, file_path: str):
        """Armazena o caminho do PDF e verifica se ele existe antes de processar."""
        if not os.path.exists(file_path):
            print(f"❌ ERRO: O arquivo '{file_path}' não foi encontrado!")
            return
        
        self.file_path = file_path
        self.description = f"Conversor Docling para o PDF: {file_path}"
        print(f"✅ Caminho do PDF armazenado corretamente: {file_path}")

    def _run(self, query: Optional[str] = None) -> str:
        """Executa a conversão do PDF para Markdown e retorna o conteúdo."""
        if not self.file_path:
            return "❌ Erro: Nenhum arquivo PDF foi adicionado à ferramenta."

        try:
            print(f"🔍 Convertendo PDF: {self.file_path}")
            converter = DocumentConverter()
            result = converter.convert(self.file_path)
            markdown_content = result.document.export_to_markdown()

            if not markdown_content.strip():
                return "⚠️ O PDF foi convertido, mas o conteúdo está vazio."

            return markdown_content
        except Exception as e:
            return f"❌ Erro ao converter PDF: {str(e)}"
