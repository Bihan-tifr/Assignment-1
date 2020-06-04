#include <stdio.h>
#include <gsl/gsl_linalg.h>

int main(void)
{
    double a_data[] = { 1,0.67,0.33,
		        0.45,1,0.55,
		        0.67,0.33,1 };

    double b_data[] = { 2,2,2 };

    gsl_matrix_view m = gsl_matrix_view_array(a_data, 3, 3);
    gsl_vector_view b = gsl_vector_view_array(b_data, 3);

    gsl_vector *x = gsl_vector_alloc(3);
    gsl_matrix *L = gsl_matrix_alloc(3,3);


    gsl_permutation *p = gsl_permutation_alloc(3);

    int s;
    gsl_linalg_LU_decomp(&m.matrix, p, &s);
    gsl_linalg_LU_solve(&m.matrix, p, &b.vector, x);

    printf("x = \n");
    gsl_vector_fprintf(stdout, x, "%g");

    gsl_permutation_free(p);

    return 0;
}
