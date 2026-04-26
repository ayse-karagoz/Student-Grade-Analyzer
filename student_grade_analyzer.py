import numpy as np

def calculate_exams(grades : list):
    return 0.4 * grades[:, 0] + 0.6 * grades[:, 1]
def is_passed(results):
    avg = np.mean(results)
    passed = results[results >= avg]
    failed = results[(results < avg) | (results < 50)]
    return passed, failed, avg
def high_5_students (passed):
    top_5 = np.sort(passed)[-5:]
    return top_5
def main ():
    grades = np.random.randint(0,100,200).reshape(100,2)
    results = calculate_exams(grades)
    passed, failed, avg = is_passed(results)
    top5 = high_5_students(results)

    print("Sınıf ortalaması:", avg)
    print("Geçen sayısı:", passed.size)
    print("Kalan sayısı:", failed.size)
    print("Top 5:", top5)
main()