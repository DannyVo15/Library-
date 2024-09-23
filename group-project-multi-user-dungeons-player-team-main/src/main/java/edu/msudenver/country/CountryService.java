package edu.msudenver.country;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;
import java.util.List;
import java.util.NoSuchElementException;

@Service
public class CountryService {
    @Autowired
    private CountryRepository countryRepository;

    @PersistenceContext
    protected EntityManager entityManager;

    public List<Country> getCountries() {
        return countryRepository.findAll();
    }

    public Country getCountry(String countryCode) {
        try {
            return countryRepository.findById(countryCode).get();
        } catch(NoSuchElementException | IllegalArgumentException e) {
            e.printStackTrace();
            return null;
        }
    }

    @Transactional
    public Country saveCountry(Country country) {
        country = countryRepository.saveAndFlush(country);
        entityManager.refresh(country);
        return country;
    }

    public boolean deleteCountry(String countryCode) {
        try {
            if(countryRepository.existsById(countryCode)) {
                countryRepository.deleteById(countryCode);
                return true;
            }
        } catch(IllegalArgumentException e) {
            e.printStackTrace();
        }

        return false;
    }
}
