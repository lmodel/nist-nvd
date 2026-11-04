package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A score under CVSS version 4.0.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvssV40  {

  private String version;
  private String vectorString;
  private String attackVector;
  private String attackComplexity;
  private String privilegesRequired;
  private String userInteraction;
  private String confidentialityRequirement;
  private String integrityRequirement;
  private String availabilityRequirement;
  private String modifiedAttackVector;
  private String modifiedAttackComplexity;
  private String modifiedPrivilegesRequired;
  private String modifiedUserInteraction;
  private String attackRequirements;
  private String vulnConfidentialityImpact;
  private String vulnIntegrityImpact;
  private String vulnAvailabilityImpact;
  private String subConfidentialityImpact;
  private String subIntegrityImpact;
  private String subAvailabilityImpact;
  private String exploitMaturity;
  private String modifiedAttackRequirements;
  private String modifiedVulnConfidentialityImpact;
  private String modifiedVulnIntegrityImpact;
  private String modifiedVulnAvailabilityImpact;
  private String modifiedSubConfidentialityImpact;
  private String modifiedSubIntegrityImpact;
  private String modifiedSubAvailabilityImpact;
  private String safety;
  private String automatable;
  private String recovery;
  private String valueDensity;
  private String vulnerabilityResponseEffort;
  private String providerUrgency;
  private float baseScore;
  private String baseSeverity;


}