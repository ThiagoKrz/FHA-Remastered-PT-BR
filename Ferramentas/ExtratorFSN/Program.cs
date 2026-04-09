using System;
using System.IO;
using System.Linq;
using System.Security.Cryptography;

class FSExtract
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Arraste um .dat, .txt, ou uma pasta _extract para o executavel.\nPressione ENTER para sair...");
            Console.ReadLine();
            return;
        }

        string inputPath = args[0];

        if (Directory.Exists(inputPath))
        {
            RepackDefinitivo(inputPath);
        }
        else if (File.Exists(inputPath))
        {
            Extract(inputPath);
        }
    }

    static void Extract(string inputFile)
    {
        string filelist;
        string dataFile;

        if (inputFile.EndsWith(".dat"))
        {
            filelist = Path.Combine(Path.GetDirectoryName(inputFile), $"fileinfo_{Path.GetFileNameWithoutExtension(inputFile)}.txt");
            dataFile = inputFile;
        }
        else if (inputFile.EndsWith(".txt"))
        {
            filelist = inputFile;
            dataFile = inputFile.Replace("fileinfo_", "").Replace(".txt", ".dat");
        }
        else return;

        var data = File.ReadAllLines(filelist).Select(line => line.Split(new[] { "::" }, StringSplitOptions.None)).ToList();
        string outputFolder = inputFile + "_extract";
        Directory.CreateDirectory(outputFolder);

        using (var arcData = new BinaryReader(File.OpenRead(dataFile)))
        {
            foreach (var file in data)
            {
                if (file.Length < 5) continue;
                string filename = Path.Combine(outputFolder, $"{file[0]}.{file[1]}");
                Console.WriteLine("Extraindo: " + file[0] + "." + file[1]);
                using (var outputFile = new FileStream(filename, FileMode.Create, FileAccess.Write))
                {
                    long start = long.Parse(file[3]);
                    int length = int.Parse(file[4]);
                    arcData.BaseStream.Seek(start, SeekOrigin.Begin);
                    byte[] buffer = arcData.ReadBytes(length);
                    outputFile.Write(buffer, 0, buffer.Length);
                }
            }
        }
        Console.WriteLine("Extracao concluida!");
    }

    static void RepackDefinitivo(string inputFolder)
    {
        inputFolder = inputFolder.TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
        if (!inputFolder.EndsWith("_extract")) return;

        string baseDatName = Path.GetFileName(inputFolder).Replace("_extract", "");
        string baseNameWithoutExt = Path.GetFileNameWithoutExtension(baseDatName);
        string parentDir = Path.GetDirectoryName(inputFolder);

        // Puxa o seu "fileinfo_ex_pack.txt"
        string originalFilelist = Path.Combine(parentDir, $"fileinfo_{baseNameWithoutExt}.txt");

        if (!File.Exists(originalFilelist))
        {
            Console.WriteLine("Erro: fileinfo.txt original nao encontrado!");
            return;
        }

        var originalData = File.ReadAllLines(originalFilelist)
                           .Select(line => line.Split(new[] { "::" }, StringSplitOptions.None))
                           .ToList();

        string newDatFile = Path.Combine(parentDir, $"REPACK_{baseDatName}");
        string newFilelist = Path.Combine(parentDir, $"REPACK_fileinfo_{baseNameWithoutExt}.txt");

        using (var outDatStream = new FileStream(newDatFile, FileMode.Create, FileAccess.Write))
        using (var outTxtStream = new StreamWriter(newFilelist))
        {
            long currentOffset = 0;

            foreach (var file in originalData)
            {
                if (file.Length < 6) continue;

                string filename = Path.Combine(inputFolder, $"{file[0]}.{file[1]}");

                // Se o arquivo sumir da pasta, o script pula ele
                if (!File.Exists(filename))
                {
                    Console.WriteLine($"[AVISO] {file[0]} ausente na pasta. Pulando...");
                    continue;
                }

                byte[] fileBytes = File.ReadAllBytes(filename);
                int length = fileBytes.Length;
                
                // Calcula o Hash exato que a engine exige
                string novoMD5 = CalcularMD5(fileBytes);

                // Sobrescreve apenas as coordenadas e a segurança
                file[3] = currentOffset.ToString();
                file[4] = length.ToString();
                file[5] = novoMD5; 

                // Escreve a nova linha reconstruindo com as variáveis originais intactas
                outTxtStream.WriteLine(string.Join("::", file));
                
                // Grava a imagem no novo .dat
                outDatStream.Write(fileBytes, 0, length);
                
                Console.WriteLine($"Empacotado: {file[0]}.{file[1]} | Hash: {novoMD5}");
                
                currentOffset += length;
            }
        }
        Console.WriteLine("\nRepack concluido com sucesso! Hash e offsets atualizados.");
    }

    static string CalcularMD5(byte[] input)
    {
        // Calcula quantos bytes faltam para o tamanho ser múltiplo de 4
        int padding = (4 - (input.Length % 4)) % 4; 
        
        // Cria um novo buffer simulando a memória da engine (Bytes originais + Zeros fantasmas)
        byte[] bufferForHash = new byte[input.Length + padding];
        Array.Copy(input, bufferForHash, input.Length);
        
        using (MD5 md5 = MD5.Create())
        {
            byte[] hashBytes = md5.ComputeHash(bufferForHash);
            return string.Join("", hashBytes.Select(b => b.ToString("x2")));
        }
    }
}