package edu.msudenver.country;

import org.apache.commons.lang3.exception.ExceptionUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/countries")
public class CountryController {
    @Autowired
    private CountryService countryService;

    @GetMapping(produces = "application/json")
    public ResponseEntity<List<Country>> getCountries() {
        try {
            return ResponseEntity.ok(countryService.getCountries());
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "/{countryCode}", produces = "application/json")
    public ResponseEntity<Country> getCountry(@PathVariable String countryCode) {
        try {
            Country country = countryService.getCountry(countryCode);
            return new ResponseEntity<>(country, country == null ? HttpStatus.NOT_FOUND : HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }

    @PostMapping(consumes = "application/json", produces = "application/json")
    public ResponseEntity<Country> createCountry(@RequestBody Country country) {
        try {
            return new ResponseEntity<>(countryService.saveCountry(country), HttpStatus.CREATED);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }

    @PutMapping(path = "/{countryCode}", consumes = "application/json", produces = "application/json")
    public ResponseEntity<Country> updateCountry(@PathVariable String countryCode, @RequestBody Country updatedCountry) {
        Country retrievedCountry = countryService.getCountry(countryCode);
        if (retrievedCountry != null) {
            retrievedCountry.setCountryName(updatedCountry.getCountryName());
            try {
                return ResponseEntity.ok(countryService.saveCountry(retrievedCountry));
            } catch (Exception e) {
                e.printStackTrace();
                return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
            }
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @DeleteMapping(path = "/{countryCode}")
    public ResponseEntity<Void> deleteCountry(@PathVariable String countryCode) {
        try {
            return new ResponseEntity<>(countryService.deleteCountry(countryCode) ? HttpStatus.NO_CONTENT : HttpStatus.NOT_FOUND);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity(ExceptionUtils.getStackTrace(e), HttpStatus.BAD_REQUEST);
        }
    }
}
