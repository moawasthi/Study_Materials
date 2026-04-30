using System.IO;
using System.Linq;

var filePath = @"D:\03_Study\Model_For_Demo\Csv_with_descriptions.csv";

var lines = File.ReadAllLines(filePath);

// Skip header row
foreach (var line in lines.Skip(1))
{
    var parts = line.Split(',');

    if (parts.Length < 3) continue;

    var tableName = parts[0].Trim();
    var columnName = parts[1].Trim();
    var description = parts[2].Trim();

    var table = Model.Tables.FindByName(tableName);
    if (table == null)
    {
       
        continue;
    }

    var column = table.Columns.FindByName(columnName);

    if (column != null)
    {
        column.Description = description;
        continue;
    }

    var measure = table.Measures.FindByName(columnName);

    if (measure != null)
    {
        measure.Description = description;
        continue;
    }
}

