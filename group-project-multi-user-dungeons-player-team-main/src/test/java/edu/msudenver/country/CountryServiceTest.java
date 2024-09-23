package edu.msudenver.country;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

@ExtendWith(SpringExtension.class)
@WebMvcTest(value = CountryService.class)
public class CountryServiceTest {

    @MockBean
    private CountryRepository countryRepository;

    @MockBean
    private EntityManagerFactory entityManagerFactory;

    @MockBean
    private EntityManager entityManager;

    @Autowired
    private CountryService countryService;

    @BeforeEach
    public void setup() {
        countryService.entityManager = entityManager;
    }

    @Test
    public void testGetCountries() throws Exception {
        Country testCountry = new Country();
        testCountry.setCountryCode("us");
        testCountry.setCountryName("United States");

        Mockito.when(countryRepository.findAll()).thenReturn(Arrays.asList(testCountry));

        List<Country> countries = countryService.getCountries();
        assertEquals(1, countries.size());
        assertEquals("United States", countries
                .get(0)
                .getCountryName());
    }

    @Test
    public void testGetCountry() throws Exception {
        Country testCountry = new Country();
        testCountry.setCountryCode("us");
        testCountry.setCountryName("United States");

        Mockito.when(countryRepository.findById(Mockito.anyString())).thenReturn(Optional.of(testCountry));
        Country country = countryService.getCountry("us");
        assertEquals("United States", country.getCountryName());
   }

    @Test
    public void testGetCountryNotFound() throws Exception {
        Mockito.when(countryRepository.findById(Mockito.anyString())).thenReturn(Optional.empty());

        assertEquals(null,
                countryService.getCountry("notfound"));
    }

    @Test
    public void testSaveCountry() throws Exception {
        Country canada = new Country();
        canada.setCountryName("Canada");
        canada.setCountryCode("ca");

        Mockito.when(countryRepository.saveAndFlush(Mockito.any())).thenReturn(canada);
        Mockito.when(countryRepository.save(Mockito.any())).thenReturn(canada);

        assertEquals(canada, countryService.saveCountry(canada));
    }

    @Test
    public void testSaveCountryBadRequest() throws Exception {
        Country badCanada = new Country();
        badCanada.setCountryName("Canada");

        Mockito.when(countryRepository.save(Mockito.any())).thenThrow(IllegalArgumentException.class);
        Mockito.when(countryRepository.saveAndFlush(Mockito.any())).thenThrow(IllegalArgumentException.class);

        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            countryService.saveCountry(badCanada);
        });
    }

    @Test
    public void testDeleteCountry() throws Exception {
        Country canada = new Country();
        canada.setCountryName("Canada");
        canada.setCountryCode("ca");
        Mockito.when(countryRepository.findById(Mockito.any())).thenReturn(Optional.of(canada));
        Mockito.when(countryRepository.existsById(Mockito.any())).thenReturn(true);

        assertTrue(countryService.deleteCountry("ca"));
    }

    @Test
    public void testDeleteCountryNotFound() throws Exception {
        Mockito.when(countryRepository.findById(Mockito.any())).thenReturn(Optional.empty());
        Mockito.when(countryRepository.existsById(Mockito.any())).thenReturn(false);
        Mockito.doThrow(IllegalArgumentException.class)
                .when(countryRepository)
                .deleteById(Mockito.any());

        assertFalse(countryService.deleteCountry("notfound"));
    }
}
