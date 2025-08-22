using Newtonsoft.Json;

namespace imaginary_schooldatabase
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Student> students = new List<Student>()
            {
                new Student("Lukas", "Martines", 'A', new DateTime(2012, 5, 12)),
                new Student("Mateo", "Perec", 'B', new DateTime(2010, 9, 3)),
                new Student("Isabella", "Rodriges", 'C', new DateTime(2014, 2, 14)),
            };

            JsonSerializerSettings settings = new JsonSerializerSettings();
            settings.Formatting = Formatting.Indented;
            string output = JsonConvert.SerializeObject(students, settings);
            File.WriteAllText(Directory.GetCurrentDirectory() + "\\students.json", output);
        }
    }
}